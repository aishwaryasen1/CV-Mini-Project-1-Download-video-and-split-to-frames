import imageio

src_dir = "C:/Users/Dell/Desktop/Frames/filename.mp4"
dst_dir = "C:/Users/Dell/Desktop/Frames/AVI.avi"

reader = imageio.get_reader(src_dir)
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer(dst_dir, fps=fps)

for im in reader:
    writer.append_data(im[:, :, :])
writer.close()