import numpy as np
from PIL import Image
import plotly.graph_objects as go

def build_globe_mesh(texture_file="data/earth.jpg", R=1.0, resize=(360,180)):
    """
    Создает цветной глобус (Mesh3d) с текстурой.
    
    texture_file - путь к файлу текстуры
    R            - радиус сферы
    resize       - размер изображения для ускорения рендера
    """
    img = Image.open(texture_file)
    img = img.resize(resize)
    texture = np.array(img)[::-1, :, :]  # переворачиваем вертикально

    n_lon, n_lat = texture.shape[1], texture.shape[0]
    lon = np.linspace(-np.pi, np.pi, n_lon)
    lat = np.linspace(-np.pi/2, np.pi/2, n_lat)
    lon, lat = np.meshgrid(lon, lat)

    X = (R * np.cos(lat) * np.cos(lon)).flatten()
    Y = (R * np.cos(lat) * np.sin(lon)).flatten()
    Z = (R * np.sin(lat)).flatten()

    colors = ["rgb({}, {}, {})".format(r, g, b) 
              for r, g, b in texture.reshape(-1, 3)]

    I, J, K = [], [], []
    for i in range(n_lat-1):
        for j in range(n_lon-1):
            idx = i * n_lon + j
            I.append(idx)
            J.append(idx + 1)
            K.append(idx + n_lon)
            I.append(idx + 1)
            J.append(idx + n_lon + 1)
            K.append(idx + n_lon)

    mesh = go.Mesh3d(
        x=X, y=Y, z=Z,
        i=I, j=J, k=K,
        vertexcolor=colors,
        flatshading=True,
        opacity=1.0
    )

    return mesh
