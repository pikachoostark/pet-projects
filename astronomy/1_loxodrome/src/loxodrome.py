import numpy as np

def loxodrome(lat0, lon0, azimuth_deg, steps=500, step_size=1.0, R=1.0, offset=0.02):
    """
    Генерация точек локсодромы на сфере.
    
    lat0, lon0      - стартовая широта и долгота (градусы)
    azimuth_deg     - курс (0-360, 0 = север, 90 = восток)
    steps           - количество шагов
    step_size       - шаг по широте (градусы)
    R               - радиус сферы
    """
    lat0 = np.radians(lat0)
    lon0 = np.radians(lon0)
    az = np.radians(azimuth_deg % 360)

    lats = [lat0]
    lons = [lon0]

    for _ in range(steps):
        # dphi положительно, если идём на север, отрицательно на юг
        dphi = np.radians(step_size) * np.cos(az)
        if abs(lats[-1] + dphi) > np.pi/2:
            break  # не выходим за полюса
        lats.append(lats[-1] + dphi)

        # d_lambda по формуле локсодромы
        if np.tan(az) != 0:
            d_lambda = dphi / np.tan(az)
        else:
            d_lambda = 0
        lons.append(lons[-1] + d_lambda)

    lats = np.array(lats)
    lons = np.array(lons)

    # Декартовы координаты
    x = (R + offset) * np.cos(lats) * np.cos(lons)
    y = (R + offset) * np.cos(lats) * np.sin(lons)
    z = (R + offset) * np.sin(lats)

    return x, y, z
