import os

import cv2
import numpy as np
from moviepy.editor import VideoFileClip, AudioFileClip

def edit_video(song_name):
    def create_formatted_video(input_video_path, output_video_path, top_text, bottom_text):
        # Open the input video
        cap = cv2.VideoCapture(input_video_path)

        # Get video properties
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Define the desired output dimensions for TikTok
        output_width = 1080
        output_height = 1920

        # Define the height for the top and bottom text boxes
        box_height = 200

        # Calculate the new dimensions of the video to fit within the TikTok format
        aspect_ratio = output_width / output_height
        video_aspect_ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        if video_aspect_ratio > aspect_ratio:
            new_width = output_width
            new_height = int(output_width / video_aspect_ratio)
        else:
            new_height = output_height - 2 * box_height
            new_width = int(new_height * video_aspect_ratio)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_video_path, fourcc, fps, (output_width, output_height))

        # Define the font and text parameters
        font = cv2.FONT_HERSHEY_SIMPLEX
        max_font_scale = 3
        font_thickness = 6
        text_color = (0, 0, 0)  # Black color
        max_text_width = new_width - 40  # Maximum width for text box

        # Function to draw centered text with dynamic font size
        def draw_centered_text(img, text, position, font, max_font_scale, color, thickness, max_width):
            # Split text into lines based on max_width
            lines = []
            line = ''
            for word in text.split():
                if cv2.getTextSize(line + word, font, max_font_scale, thickness)[0][0] <= max_width:
                    line += word + ' '
                else:
                    lines.append(line)
                    line = word + ' '
            lines.append(line)

            # Calculate starting y position for text
            text_height = len(lines) * (cv2.getTextSize('A', font, max_font_scale, thickness)[0][1] -50)
            text_y = position + (box_height - text_height) // 2 + 150

            # Draw each line of text
            for line in lines:
                text_size = cv2.getTextSize(line.strip(), font, max_font_scale, thickness)[0]
                text_x = (img.shape[1] - text_size[0]) // 2
                cv2.putText(img, line.strip(), (text_x, text_y), font, max_font_scale, color, thickness,
                            lineType=cv2.LINE_AA)
                text_y += text_size[1] + 40

        # Process each frame
        for _ in range(frame_count):
            ret, frame = cap.read()
            if not ret:
                break

            # Resize the frame to fit the new dimensions
            frame = cv2.resize(frame, (new_width, new_height))

            # Create a new frame with the extra space for top and bottom boxes
            new_frame = np.ones((output_height, output_width, 3), dtype=np.uint8) * 255  # White background

            # Place the resized video frame in the center
            y_offset = box_height + (output_height - 2 * box_height - new_height) // 2
            x_offset = (output_width - new_width) // 2
            new_frame[y_offset:y_offset + new_height, x_offset:x_offset + new_width] = frame

            # Draw the top text centered in the top box
            draw_centered_text(new_frame, top_text, 0, font, max_font_scale, text_color, font_thickness, max_text_width)

            # Draw the bottom text centered in the bottom box
            draw_centered_text(new_frame, bottom_text, output_height - box_height-300, font, max_font_scale, text_color,
                               font_thickness, max_text_width)

            # Write the frame to the output video
            out.write(new_frame)

        # Release everything if job is finished
        cap.release()
        out.release()


    # Example usage
    input_video_path = "C:\\Users\\Mawan\\PycharmProjects\\ContentGenerator\\Videos\\temp\\input.mp4"
    output_video_path = 'C:\\Users\\Mawan\\PycharmProjects\\ContentGenerator\\Videos\\done\\output_video.mp4'
    top_text = "Finding songs which I Heard\r But Forgot"
    bottom_text = 'Song Name: '+ song_name


    create_formatted_video(input_video_path, output_video_path, top_text, bottom_text)

    video_clip = VideoFileClip(output_video_path)
    audio_clip = AudioFileClip(input_video_path)
    temp_audio_file = "temp_audio.wav"
    audio_clip.write_audiofile(temp_audio_file, codec="pcm_s16le")

    audio_clip_modified = audio_clip.volumex(1)

    final_clip = video_clip.set_audio(audio_clip_modified)

    final_clip.write_videofile("Videos\\"+song_name+".mp4", codec="libx264", audio_codec="aac")
    os.remove(input_video_path)
