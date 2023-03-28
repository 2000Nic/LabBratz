import cv2

class Blob_Detector:

    def __init__(self, image):
        self.setup()
        image = image[2:-1] + image[-1]
        self.im = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        self.im = ~self.im

    def setup(self):
        params = cv2.SimpleBlobDetector_Params()
        # Change thresholds
        params.minThreshold = 10
        params.maxThreshold = 200

        # Filter by Area.
        params.filterByArea = True
        params.minArea = 10

        # Filter by Circularity
        params.filterByCircularity = True
        params.minCircularity = 0.1

        # Filter by Convexity
        params.filterByConvexity = True
        params.minConvexity = 0.9

        # Filter by Inertia
        params.filterByInertia = True
        params.minInertiaRatio = 0.000000000000000000001

        # Create a detector with the parameters
        # OLD: detector = cv2.SimpleBlobDetector(params)
        self.detector = cv2.SimpleBlobDetector_create(params)

    def detect(self):
        # Detect blobs.
        keypoints = self.detector.detect(self.im)
        return keypoints



