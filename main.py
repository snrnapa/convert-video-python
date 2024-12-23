from moviepy import VideoFileClip
import os


def mov2mp4(file_dir: str, output_file_name: str) -> None:
    output_dir = "./data/out"
    # 入力ファイルと出力ファイルを指定
    output_file = output_dir + "/" + output_file_name + ".mp4"

    # 動画情報を取得
    video_clip = VideoFileClip(file_dir)

    # 解像度を取得
    width = video_clip.size[0]
    height = video_clip.size[1]
    rotation = video_clip.rotation
    fps = video_clip.fps
    duration = video_clip.duration
    print("video_clip.size:", width, height, rotation, fps, duration)

    # MOV動画をMP4に変換して保存
    if rotation == 90:
        video_clip.write_videofile(
            output_file,
            codec="libx264",
            ffmpeg_params=["-vf", f"scale={height}:{width}"],
        )
    else:
        video_clip.write_videofile(
            output_file,
            codec="libx264",
            ffmpeg_params=["-vf", f"scale={width}:{height}"],
        )


def main() -> None:
    input_data_dir = "./data/in"
    movie_file_list = os.listdir(input_data_dir)
    for file in movie_file_list:
        print(f"{file}の変換を開始します")
        file_dir = input_data_dir + "/" + file
        file_name = file.split(".")[0]
        mov2mp4(file_dir, file_name)
        print(f"{file}の変換が完了しました")


if __name__ == "__main__":
    main()
