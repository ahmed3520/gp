from src.modelFetch import modelImageFetch

def testSpiralImage(link):
    classes_x = modelImageFetch(link, "cnn.h5", 224, 224)

    return classes_x