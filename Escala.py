import os
from PIL import Image
import matplotlib.pyplot as plt


INPUT_FOLDER = "Entrada"
OUTPUT_FOLDER = "Saida"


def lerEntrada(filename):
    return os.path.join(INPUT_FOLDER, filename)


def salvarSaida(filename):
    return os.path.join(OUTPUT_FOLDER, filename)


def alterarEscalaCinza_mediaSimples(imagemOriginalColorida):
    largura, altura = imagemOriginalColorida.size
    imagemAlterada = Image.new("RGB", (largura, altura))

    for x in range(largura):
        for y in range(altura):
            coordenadaPixel = imagemOriginalColorida.getpixel((x, y))
            cinzaMedio = (
                coordenadaPixel[0] + coordenadaPixel[1] + coordenadaPixel[2])//2
            imagemAlterada.putpixel(
                (x, y), (cinzaMedio, cinzaMedio, cinzaMedio))
    return imagemAlterada


def filtroDeMediaSimples(imagemOriginal):
    largura, altura = imagemOriginal.size
    imagemAlterada = Image.new("RGB", (largura, altura))

    for x in range(largura - 2):
        for y in range(altura - 2):
            pixel1 = imagemOriginal.getpixel((x-1, y+1))
            pixel2 = imagemOriginal.getpixel((x, y+1))
            pixel3 = imagemOriginal.getpixel((x+1, y+1))
            pixel4 = imagemOriginal.getpixel((x-1, y))
            pixelCentral = imagemOriginal.getpixel((x, y))
            pixel6 = imagemOriginal.getpixel((x+1, y))
            pixel7 = imagemOriginal.getpixel((x-1, y-1))
            pixel8 = imagemOriginal.getpixel((x, y-1))
            pixel9 = imagemOriginal.getpixel((x+1, y-1))
            cor1 = (pixel1[0] + pixel1[1] + pixel1[2])//3
            cor2 = (pixel2[0] + pixel2[1] + pixel2[2])//3
            cor3 = (pixel3[0] + pixel3[1] + pixel3[2])//3
            cor4 = (pixel4[0] + pixel4[1] + pixel4[2])//3
            cor5 = (pixelCentral[0] + pixelCentral[1] + pixelCentral[2])//3
            cor6 = (pixel6[0] + pixel6[1] + pixel6[2])//3
            cor7 = (pixel7[0] + pixel7[1] + pixel7[2])//3
            cor8 = (pixel8[0] + pixel8[1] + pixel8[2])//3
            cor9 = (pixel9[0] + pixel9[1] + pixel9[2])//3
            corNova = ((cor1 + cor2 + cor3 + cor4 +
                       cor5 + cor6 + cor7 + cor8 + cor9))//9

            imagemAlterada.putpixel((x, y), (corNova, corNova, corNova))
    return imagemAlterada


def filtroDeMediaPonderada(imagemOriginal):
    largura, altura = imagemOriginal.size
    imagemAlterada = Image.new("RGB", (largura, altura))

    for x in range(largura - 2):
        for y in range(altura - 2):
            pixel1 = imagemOriginal.getpixel((x-1, y+1))
            pixel2 = imagemOriginal.getpixel((x, y+1))
            pixel3 = imagemOriginal.getpixel((x+1, y+1))
            pixel4 = imagemOriginal.getpixel((x-1, y))
            pixelCentral = imagemOriginal.getpixel((x, y))
            pixel6 = imagemOriginal.getpixel((x+1, y))
            pixel7 = imagemOriginal.getpixel((x-1, y-1))
            pixel8 = imagemOriginal.getpixel((x, y-1))
            pixel9 = imagemOriginal.getpixel((x+1, y-1))
            cor1 = (30*pixel1[0] + 59*pixel1[1] + 11*pixel1[2])//100
            cor2 = (30*pixel2[0] + 59*pixel2[1] + 11*pixel2[2])//100
            cor3 = (30*pixel3[0] + 59*pixel3[1] + 11*pixel3[2])//100
            cor4 = (30*pixel4[0] + 59*pixel4[1] + 11*pixel4[2])//100
            cor5 = (30*pixelCentral[0] + 59 *
                    pixelCentral[1] + 11*pixelCentral[2])//100
            cor6 = (30*pixel6[0] + 59*pixel6[1] + 11*pixel6[2])//100
            cor7 = (30*pixel7[0] + 59*pixel7[1] + 11*pixel7[2])//100
            cor8 = (30*pixel8[0] + 59*pixel8[1] + 11*pixel8[2])//100
            cor9 = (30*pixel9[0] + 59*pixel9[1] + 11*pixel9[2])//100
            corNova = ((cor1 + cor2 + cor3 + cor4 +
                       cor5 + cor6 + cor7 + cor8 + cor9))//9

            imagemAlterada.putpixel((x, y), (corNova, corNova, corNova))
    return imagemAlterada


def filtroDeMediana(imagemOriginal):
    largura, altura = imagemOriginal.size
    ImagemAlterada = Image.new("RGB", (largura, altura))
    for x in range(largura-2):
        for y in range(altura-2):
            pixel1 = imagemOriginal.getpixel((x-1, y+1))
            pixel2 = imagemOriginal.getpixel((x, y+1))
            pixel3 = imagemOriginal.getpixel((x+1, y+1))
            pixel4 = imagemOriginal.getpixel((x-1, y))
            pixel5 = imagemOriginal.getpixel((x, y))
            pixel6 = imagemOriginal.getpixel((x+1, y))
            pixel7 = imagemOriginal.getpixel((x-1, y-1))
            pixel8 = imagemOriginal.getpixel((x, y-1))
            pixel9 = imagemOriginal.getpixel((x+1, y-1))
            p1 = (pixel1[0] + pixel1[1] + pixel1[2])//3
            p2 = (pixel2[0] + pixel2[1] + pixel2[2])//3
            p3 = (pixel3[0] + pixel3[1] + pixel3[2])//3
            p4 = (pixel4[0] + pixel4[1] + pixel4[2])//3
            p5 = (pixel5[0] + pixel5[1] + pixel5[2])//3
            p6 = (pixel6[0] + pixel6[1] + pixel6[2])//3
            p7 = (pixel7[0] + pixel7[1] + pixel7[2])//3
            p8 = (pixel8[0] + pixel8[1] + pixel8[2])//3
            p9 = (pixel9[0] + pixel9[1] + pixel9[2])//3

            valores = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
            valores.sort()
            valorPixelCentral = valores[4]
            ImagemAlterada.putpixel(
                (x, y), (valorPixelCentral, valorPixelCentral, valorPixelCentral))

    return ImagemAlterada


if __name__ == "__main__":
    imagemOriginal = Image.open(lerEntrada("mulher.jfif"))
    imagemNovaMedia = filtroDeMediaSimples(imagemOriginal)
    imagemNovaMedia.save(salvarSaida("mulherMedia.jfif"))

    imagemNovaMediana = filtroDeMediana(imagemOriginal)
    imagemNovaMediana.save(salvarSaida("mulherMediana.jfif"))

    imagemOriginal.show()
    imagemNovaMedia.show()
    imagemNovaMediana.show()
