import numpy as np
import random

class IO_Utils:

    def image_crop(self, im, gt, width, height, num_crop):
        """
        :param im: The image (as a numpy array of pixels) to crop.
                    It is assumed to have dimensions:
                    (WxHxD) where:
                    W = Image width
                    H = Image height
                    D = Image depth (usually 3 for 3 colour channels)
        :param gt: The ground truth labelling of im (as a numpy array of pixels) to crop.
                    It is assumed to have dimensions:
                    (WxHxD) where:
                    W = Image width
                    H = Image height
                    D = Image depth (usually 3 for 3 colour channels)
        :param width: The desired width in the cropped image.
        :param height: The desired height in the cropped image.
        :return: images: A numpy array of randomly sampled cropped portion of the input image.
                The cropped images will have dimensions:
                (width x height x D). There will be num_crop of them. So images has dimension:
                (width x height x D x num_crop)
        :return: gt_images: A numpy array of randomly sampled cropped portion of the corresponding ground truth for an input image.
                The cropped images will have dimensions:
                (width x height x D). There will be num_crop of them. So gt_images has dimension:
                (width x height x D x num_crop)
        """

        x = im.shape[0]
        y = im.shape[1]
        d = im.shape[2]
        images = np.zeros((width, height, d, num_crop))
        gt_images = np.zeros_like(images)
        index_map = np.zeros((x, y))
        n = 0
        while n < num_crop:
            i = random.randrange(0, x)
            j = random.randrange(0, y)
            #This map is used to ensure that we don't
            #use the same (i,j) pair twice.
            if index_map[i,j] == 0:
                index_map[i,j] = 1
            else:
                continue
            width_0 = i - (width/2)
            width_1 = i + (width/2)
            height_0 = j - (height/2)
            height_1 = j + (height/2)
            if width_0 > 0 and width_1 < x:
                if height_0 > 0 and height_1 < y:
                    images[:,:,:,n]= \
                    im[width_0:width_1, height_0:height_1, :]
                    gt_images[:,:,:,n] = \
                    gt[width_0:width_1, height_0:height_1, :]
                    n += 1

        return images, gt_images

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

#Used for testing:

#     def main(self):
#         from PIL import Image
#         im = Image.open('aerial_photo.jpg')
#         #im = self.image_scale(im, 256)
#         array = np.array(im)
#         n = 6
#         array_of_images,_ = self.image_crop(array, array, 256, 256, n)
#         #array = self.image_rotate(array)
#         #array = self.image_flip_vertical(im)
#         print array_of_images.shape
#         for i in xrange(n):
#             im = Image.fromarray(np.uint8(array_of_images[:,:,:,i]))
#             im.show()
#
# if __name__ == "__main__":
#     io_utils = IO_Utils()
#     io_utils.main()