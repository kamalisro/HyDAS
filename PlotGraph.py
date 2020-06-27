from OpenGL.raw.GL.ARB.draw_indirect import _f

__author__ = 'Lalit Kumar'

import pyqtgraph as pg
from spectral import *
from ZProf import Viewdef, FileName
from NewWin import ChangeValue
from osgeo import gdal
from osgeo import osr


class PG:
    plotItem = None

    @staticmethod
    def zprof():
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        PG.plotItem = pg.plot(title="Z-Profile (Viewer 1)")

    @staticmethod
    def plotGraph(File, pixx, pixy):
        if Viewdef.Zprof > 0:
            PG.plotItem.clear()
            im = open_image(str(File))
            y = im.read_pixel(pixy, pixx)
            hdrmetadata = im.metadata
            wavelengthinStr = hdrmetadata.get('wavelength')
            x = []
            for i in range(0, len(wavelengthinStr)):
                x.append(float(wavelengthinStr[i]))
            try:
                # PG.plotItem = pg.plot(title="Spectra Visualisation")
                # PG.plotItem.hideAxis('top')
                PG.plotItem.setLabel('top', text=" Co-ordinates: (" + str(pixx) + "," + str(pixy) + ")")
                PG.plotItem.showGrid(x=True, y=True, alpha=0.5)
                PG.plotItem.setLabel('bottom', text="Wavelength")
                PG.plotItem.setLabel('left', text="Reflectance")
                PG.plotItem.showAxis('bottom')
                PG.plotItem.showAxis('left')
                PG.plotItem.plot(x, y, pen=(1, 1))


            except Exception, e:
                print e

    @staticmethod
    def showinfo(x, y, rgb=''):
        file1 = str(FileName.File)
        file= file1[0:len(file1)-4]
        ds = gdal.Open(file)
        xoff, a, b, yoff, d, e = ds.GetGeoTransform()
        Mapx = a * x + b * y + xoff
        Mapy = d * x + e * y + yoff
        gt = ds.GetGeoTransform()
        srs = osr.SpatialReference()
        srs.ImportFromWkt(ds.GetProjection())
        srsLatLong = srs.CloneGeogCS()
        ct = osr.CoordinateTransformation(srs, srsLatLong)
        ulon = x * gt[1] + gt[0]
        ulat = y * gt[5] + gt[3]
        (long, lat, holder) = ct.TransformPoint(ulon, ulat)

        degrees1 = int(lat)
        submin1 = abs( (lat - int(lat) ) * 60)
        minutes1 = int(submin1)
        subseconds1 = abs((submin1-int(submin1)) * 60)
        degrees2 = int(long)
        submin2 = abs( (long - int(long) ) * 60)
        minutes2 = int(submin2)
        subseconds2 = abs((submin2-int(submin2)) * 60)

        direction1 = ""
        direction2 = ""
        type1="Latitude"
        type2="Longitude"
        if type2 == "Longitude":
            if degrees1 < 0:
                direction1 = "W"
            elif degrees1 > 0:
                direction1 = "E"
            else:
                direction1 = ""
        if type1 == "Latitude":
            if degrees2 < 0:
                direction2 = "S"
            elif degrees2 > 0:
                direction2 = "N"
            else:
                direction2 = ""
        lati = str(degrees1)+'*'+str(minutes1)+"'"+str(subseconds1)[0:5]+'"'+ direction1
        longi= str(degrees2)+'*'+str(minutes2)+"'"+str(subseconds2)[0:5]+'"'+direction2

        ChangeValue.valueLabel.setText("\nDisplay 1:\n\n Pixel Values: "+ '('+str(x)+','+str(y)+')\n\n'+"Map: "+str(Mapx)+"E , "+str(Mapy)+"N Meters\n\n"+\
            "LL: "+str(lati)+","+str(longi)+ "\n\nR-G-B:"+str(rgb))





