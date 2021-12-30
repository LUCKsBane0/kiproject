if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    import cv2
    import glob
    from PIL import Image

    folder_path_D =glob.glob("/home/david/Downloads/drive-download-20211222T092238Z-001/Dreieck/*.png")
    cv_img_D = []
    for img in folder_path_D:
        n = cv2.imread(img,0)
        cv_img_D.append(n)
    vectors_first_D =[]
    for i in cv_img_D:
        x = np.ravel(i)
        vectors_first_D.append(x)
    num_vectors_d=np.asarray(vectors_first_D)
    np.reshape(num_vectors_d,-1)
    print(num_vectors_d.shape)
    dreieckdf=pd.DataFrame(num_vectors_d)
    dreieckdf_zeros= pd.DataFrame(np.zeros((1, 2500)))

    folder_path_K = glob.glob("/home/david/Downloads/drive-download-20211222T092238Z-001/Kreis")
    cv_img_K = []
    for img in folder_path_K:
        n = cv2.imread(img,0)
        cv_img_K.append(n)
    vectors_first_K =[]
    for i in cv_img_K:
        x = np.ravel(i)
        vectors_first_K.append(x)
    num_vectors_K=np.asarray(vectors_first_K)
    np.reshape(num_vectors_K,-1)
    print(num_vectors_K.shape)
    kreisdf=pd.DataFrame(num_vectors_K)
    kreisdf_zeros= pd.DataFrame(np.zeros((1, 2500)))
    pd.DataFrame(dreieckdf.to_csv("vectors.csv"))
    
    folder_path_H = glob.glob("/home/david/Downloads/drive-download-20211222T092238Z-001/Herz")
    cv_img_H = []
    for img in folder_path_H:
        n = cv2.imread(img,0)
        cv_img_H.append(n)
    vectors_first_H =[]
    for i in cv_img_H:
        x = np.ravel(i)
        vectors_first_H.append(x)
    num_vectors_H=np.asarray(vectors_first_H)
    np.reshape(num_vectors_H,-1)
    print(num_vectors_H.shape)
    kreisdf=pd.DataFrame(num_vectors_H)
    kreisdf_zeros= pd.DataFrame(np.zeros((1, 2500)))
    pd.DataFrame(dreieckdf.to_csv("vectors.csv"))
