import numpy as np
import random

class IO_Utils:

    def image_crop(self, im, width, height):
        """
        :param im: The image (as a numpy array of pixels) to crop.
                    It is assumed to have dimensions:
                    (WxHxD) where:
                    W = Image width
                    H = Image height
                    D = Image depth (usually 3 for 3 colour channels)
        :param width: The desired width in the cropped image.
        :param height: The desired height in the cropped image.
        :return: A randomly sampled cropped portion of the input image.
                The cropped image will have dimensions:
                (width x height x D).
        """

        cropped_Image = None
        x = im.shape[0]
        y = im.shape[1]
        while (cropped_Image == None):
            i = random.randrange(0, x)
            j = random.randrange(0, y)
            width_0 = i - (width/2)
            width_1 = i + (width/2)
            height_0 = j - (height/2)
            height_1 = j + (height/2)
            if width_0 > 0 and width_1 < x:
                if height_0 > 0 and height_1 < y:
                    cropped_Image = \
                    im[width_0:width_1, height_0:height_1, :]

        return cropped_Image

    def image_flip_horizontal(self, im):
        """
        :param im: The image (as a numpy array of pixels) to crop.
                    It is assumed to have dimensions:
                    (WxHxD) where:
                    W = Image width
                    H = Image height
                    D = Image depth (usually 3 for 3 colour channels)
        :return: A copy of the image flipped horizontally about the vertical midpoint of the image.
                The flipped image will have the dimensions:
                (WxHxD)
        """
        return np.fliplr(im)

    def image_flip_vertical(self, im):
        """
        :param im: The image (as a numpy array of pixels) to crop.
                    It is assumed to have dimensions:
                    (WxHxD) where:
                    W = Image width
                    H = Image height
                    D = Image depth (usually 3 for 3 colour channels)
        :return: A copy of the image flipped vertically about the horizontal midpoint of the image.
                The flipped image will have the dimensions:
                (WxHxD)
        """
        return np.flipud(im)

    def image_rotate(self, im):
        """
        :param im: The image (as a numpy array of pixels) to crop.
                    It is assumed to have dimensions:
                    (WxHxD) where:
                    W = Image width
                    H = Image height
                    D = Image depth (usually 3 for 3 colour channels)
        :return: A rotated version of the image.
                 Note: If the image is not square then with
                 probability 0.5 the dimensions will flip.
                 i.e. with 90 or 270 degree rotations, the
                 returned image will have dimensions:
                 (HxWxD)
                 with 0 or 180 degree rotations the returned
                 image will have dimensions:
                 (WXHxD)
        """
        angles = [0,1,2,3]
        rotation_angle = random.choice(angles)
        print 'Rotation angle: ' + str(rotation_angle)
        return np.rot90(im, rotation_angle)

    def image_scale(self, im, size):
        """

        :param im: An image file to be resized.
        :param size: The dimensions to be used to scale
                    the image.
        :return: An image file with dimensions
                (size, size).
                Note: The aspect ratio is not
                maintained.
        """
        dimensions = size,size
        return im.resize(dimensions)

# Used for testing:

#     def main(self):
#         from PIL import Image
#         im = Image.open('aerial_photo.jpg')
#         im = self.image_scale(im, 256)
#         array = np.array(im)
#         #array = self.image_crop(array, 256, 256)
#         #array = self.image_rotate(array)
#         #array = self.image_flip_vertical(im)
#         print array.shape
#         im = Image.fromarray(np.uint8(array))
#         im.show()
#
# if __name__ == "__main__":
#     io_utils = IO_Utils()
#     io_utils.main()