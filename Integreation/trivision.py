from banner import show_trivision_banner

# ✅ Show banner animation only
if __name__ == "__main__":
    show_trivision_banner(animated=True, sound=False)

    import cv2
    import numpy as np
    import os
    from ultralytics import YOLO
    from insightface.app import FaceAnalysis
    from banner import play_sound  # ✅ Import sound function

    # ✅ Load models
    har_model = YOLO("C:/Users/rishi/OneDrive/Desktop/Trivision/models/HAR/best.pt")
    helmet_model = YOLO("C:/Users/rishi/OneDrive/Desktop/Trivision/models/Helmet/best.pt")
    face_model = YOLO("yolov8n.pt")
    app = FaceAnalysis(name="buffalo_l", providers=['CUDAExecutionProvider'])
    app.prepare(ctx_id=0)

    # ✅ Load known reference face embeddings
    reference_dir = "C:/Users/rishi/OneDrive/Desktop/Trivision/reference_images"
    known_embeddings = []
    known_names = []

    for filename in os.listdir(reference_dir):
        if filename.lower().endswith(('.jpg', '.png')):
            img_path = os.path.join(reference_dir, filename)
            img = cv2.imread(img_path)
            faces = app.get(img)
            if faces:
                known_embeddings.append(np.array(faces[0].normed_embedding))
                known_names.append(os.path.splitext(filename)[0])
    print("✅ Loaded reference faces:", known_names)

    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    # ✅ Start camera
    cap = cv2.VideoCapture(0)
    play_sound()  # ✅ Play sound when camera starts

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        annotated = frame.copy()

        har_results = har_model(frame)
        annotated = har_results[0].plot(img=annotated)

        helmet_results = helmet_model(frame)
        annotated = helmet_results[0].plot(img=annotated)

        face_results = face_model(frame, classes=[0])
        for det in face_results[0].boxes:
            x1, y1, x2, y2 = map(int, det.xyxy[0])
            person_crop = frame[y1:y2, x1:x2]

            faces = app.get(person_crop)
            for face in faces:
                emb = np.array(face.normed_embedding)
                name = "Unknown"
                max_sim = 0.0
                for i, known_emb in enumerate(known_embeddings):
                    sim = cosine_similarity(emb, known_emb)
                    if sim > 0.4 and sim > max_sim:
                        max_sim = sim
                        name = known_names[i]
                cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(annotated, f"{name} ({max_sim:.2f})", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("TriVision - Jetson Inspection HUD (Press 'x' to Exit)", annotated)
        if cv2.waitKey(1) & 0xFF == ord("x"):
            break

    cap.release()
    cv2.destroyAllWindows()
