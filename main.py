from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import face_recognition
import numpy as np
import json
import pandas as pd
from datetime import datetime
import pyttsx3

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Smart Attendance System")
        self.root.configure(bg="skyblue")
        
        # Load and place image
        img = Image.open(r"img3.jpg").resize((1300, 550), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=10, width=1600, height=650)
        
        # Main button to open feature window
        self.b1_1 = Button(self.root, text="Time to Check In", command=self.open_features_window, cursor="hand2", 
                      font=("times new roman", 30, "bold"), bg="blue", fg="white")
        self.b1_1.place(x=400, y=710, width=600, height=50)

        self.feature_frame=Frame(self.root,bg="white")
       # self.feature_frame.title("Smart Attendance Features")
       


    def open_features_window(self):
        #self.feature_frame = Toplevel(self.root)
        #self.feature_frame.geometry("500x400")
        #self.new_window.title("Face Recognition Features")
        self.b1_1.destroy()
        #self.feature_frame.title("Smart Attendance Features")
        self.feature_frame.place(x=880,y=70,width=500,height=250)
        
        Button(self.feature_frame, text="Capture Photos", command=self.capture_photos, font=("Arial", 14), bg="lightblue").pack(pady=10)
        Button(self.feature_frame, text="Train Data", command=self.train_data, font=("Arial", 14), bg="lightblue").pack(pady=10)
        Button(self.feature_frame, text="Recognize Face", command=self.recognize_face, font=("Arial", 14), bg="lightblue").pack(pady=10)
        Button(self.feature_frame, text="Show Attendance", command=self.show_attendance, font=("Arial", 14), bg="lightblue").pack(pady=10)

    def capture_photos(self):
        capture_window = Toplevel(self.feature_frame)
        capture_window.geometry("400x200")
        capture_window.title("Capture Photos")
        
        Label(capture_window, text="Enter Your Name:", font=("Arial", 12)).pack(pady=5)
        name_entry = Entry(capture_window, font=("Arial", 12))
        name_entry.pack(pady=5)
        
        def start_capture():
            user_name = name_entry.get().strip()
            if not user_name:
                messagebox.showerror("Error", "Please enter a name")
                return
            
            cap = cv2.VideoCapture(0)
            if not os.path.exists("dataset"):
                os.makedirs("dataset")
            count = 0
            max_photos = 50
            
            while count < max_photos:
                ret, frame = cap.read()
                if not ret:
                    messagebox.showerror("Error", "Failed to capture image")
                    break
                cv2.imshow("Capturing Photos", frame)
                count += 1
                
                filename = f"dataset/{user_name}_{count}.jpg"
                cv2.imwrite(filename, frame)
                cv2.waitKey(100)
            
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Success", "Capturing Successful")
            capture_window.destroy()
        
        Button(capture_window, text="Start Capture", command=start_capture, font=("Arial", 12), bg="green", fg="white").pack(pady=10)
    
    

    def train_data(self):
        # Create a directory for storing the embeddings
        if not os.path.exists("embeddings"):
            os.makedirs("embeddings")

        # Load the images and extract names
        image_paths = [os.path.join("dataset", f) for f in os.listdir("dataset")]
        embeddings = []
        names = []
        for image_path in image_paths:
            # Extract the name from the file path (ignoring numbering)
            name = os.path.basename(image_path).split('_')[0]
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)
            if len(face_encodings) == 1:
                embeddings.append(face_encodings[0])
                names.append(name)

        # Save the embeddings and names
        np.save("embeddings/embeddings.npy", embeddings)
        with open("embeddings/names.json", "w") as f:
            json.dump(names, f)
        messagebox.showinfo("Success", "Training Successful")
        


    def recognize_face(self):
        # Load face embeddings
        embeddings = np.load("embeddings/embeddings.npy")

        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        engine.setProperty('rate', 110)  # Slow down speech for clarity

        # Set Indian English voice
        voices = engine.getProperty('voices')
        for voice in voices:
            if "india" in voice.name.lower():  # Find an Indian English voice
                engine.setProperty('voice', voice.id)
                break

        # Initialize the camera
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            exit()

        # Ensure the attendance file exists
        if not os.path.exists("attendance.json"):
            with open("attendance.json", "w") as f:
                json.dump([], f)

        # Load attendance data
        try:
            with open("attendance.json", "r") as f:
                attendance = json.load(f)
                if not isinstance(attendance, list):  
                    attendance = []
        except (FileNotFoundError, json.JSONDecodeError):
            attendance = []

        # Load known names
        with open("embeddings/names.json", "r") as f:
            names = json.load(f)

        # Track attendance in this session
        marked_in_session = set()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Detect faces
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)

            recognized_names = []

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                matches = face_recognition.compare_faces(embeddings, face_encoding)
                face_distances = face_recognition.face_distance(embeddings, face_encoding)
                best_match_index = np.argmin(face_distances) if face_distances.size > 0 else -1

                if best_match_index != -1 and matches[best_match_index]:
                    name = names[best_match_index]

                    if name not in marked_in_session:
                        attendance.append({
                            "name": name,
                            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        })
                        marked_in_session.add(name)
                        recognized_names.append(name)

                    # Draw rectangle and show name
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, "Unknown", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

            # Show frame
            cv2.imshow("Frame", frame)

            # Announce names after they are displayed
            for name in recognized_names:
                engine.say(f"{name}, present.")
            engine.runAndWait()

            # Save attendance
            with open("attendance.json", "w") as f:
                json.dump(attendance, f, indent=4)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Recognition Complete and Attendance Marked")

        
    
    def show_attendance(self):
        df = pd.read_json("attendance.json")
        df.to_excel("attendance_log.xlsx", index=False, engine='openpyxl')
        os.startfile("attendance_log.xlsx")

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
