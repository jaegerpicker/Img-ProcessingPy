import PIL.Image as Image
import os
import settings


class Avatar(object):

    def __init__(self):
        pass

    def invalid_img(self, file_name, msg=''):
        os.remove(settings.MEDIA_ROOT + '/' + settings.AVATAR_UPLOAD_DIR + '/' + file_name)
        raise Exception(file_name + ' is not a valid image type' + msg)

    def resize_img(self, im, file_name):
        print im.size
        if im.size[0] != im.size[1]:
            print 'x != y'
            #if portait
            if im.size[0] > im.size[1]:
                print 'x > y'
                #crop image to correct size
                if im.size[0] > 200:
                    print 'x > 200'
                    half_size_x = im.size[0]/2
                    starting_left = half_size_x - 100
                    starting_right = half_size_x + 100
                    if im.size[1] > 200:
                        print 'y > 200'
                        half_size_y = im.size[1]/2
                        starting_top = half_size_y - 100
                        starting_bottom = half_size_y + 100
                    else:
                        print 'y < 200'
                        starting_top = 0
                        starting_bottom = im.size[1]
                    crop_box = (starting_left, starting_top, starting_right, starting_bottom)
                    print crop_box
                    im = im.crop(crop_box)
                    im.save(file_name)
                    return im
                scale = float(im.size[1])/float(im.size[0])
                ysize = 200 * scale
                res = (200, int(ysize))
                print 'res' + str(res)
                im = im.resize(res, Image.BILINEAR)
                im.save(file_name, im.format)
                return im
            else:
                print 'x < y'
                #crop image to correct size
                if im.size[1] > 200:
                    print 'y > 200'
                    half_size_y = im.size[1]/2
                    starting_top = half_size_y - 100
                    starting_bottom = half_size_y + 100
                    if im.size[0] > 200:
                        print 'x > 200'
                        half_size_x = im.size[0]/2
                        starting_left = half_size_x - 100
                        starting_right = half_size_x + 100
                    else:
                        print 'x < 200'
                        starting_left = 0
                        starting_right = im.size[0]
                    crop_box = (starting_left, starting_top, starting_right, starting_bottom)
                    print crop_box
                    im = im.crop(crop_box)
                    im.save(file_name)
                    return im
                scale = float(im.size[0])/float(im.size[1])
                print scale
                xscale = 200 * scale
                print xscale
                res = (int(xscale), 200)
                print 'res' + str(res)
                im = im.resize(res, Image.BILINEAR)
                im.save(file_name)
                return im
        else:
            if im.size[0] > 200:
                res = (200, 200)
                print res
                im = im.resize(res)
                print im.size
                print file_name
                print im.format
                im.save(file_name, im.format)
                print im
                return im
            else:
                im.save(file_name)
                return im


