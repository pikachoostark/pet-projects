from loxodrome import loxodrome
from globe import build_globe_mesh
import plotly.graph_objects as go
import argparse

def parse_loxodromes(raw_list):
    """
    Преобразует список строк вида lat,lon,azimuth в кортежи float.
    Азимут ограничен <90°, иначе локсодрома будет вести к Южному полюсу.
    """
    lox_list = []
    for item in raw_list:
        parts = item.split(',')
        if len(parts) != 3:
            print(f"Некорректный формат локсодромы: {item}. Пропускаем.")
            continue
        try:
            lat0, lon0, azimuth = map(float, parts)
            if not (0 <= azimuth < 90):
                print(f"Азимут {azimuth}° для локсодромы {item} вне диапазона [0.0-90.0) — пропускаем.")
                continue
            lox_list.append((lat0, lon0, azimuth))
        except ValueError:
            print(f"Ошибка преобразования чисел: {item}. Пропускаем.")
    return lox_list

def main():
    parser = argparse.ArgumentParser(description="Строим локсодромы на цветной сфере.")
    parser.add_argument("--loxodromes", type=str, nargs='+',
                        help="Список локсодром в формате lat,lon,azimuth, например: 0,0,45 10,20,90 15,60,15")
    parser.add_argument("--texture", type=str, default="data/earth.jpg",
                        help="Путь к текстуре Земли")
    parser.add_argument("--output", type=str, default="examples/loxodrome_example.html",
                        help="Имя выходного HTML-файла")
    parser.add_argument("--step_size", type=float, default=1.0, help="Шаг по широте (градусы)")
    parser.add_argument("--steps", type=int, default=800, help="Количество шагов")
    parser.add_argument("--offset", type=float, default=0.02, help="Подъем линии над сферой")
    parser.add_argument("--highres", action="store_true", help="Использовать высокое разрешение текстуры 2048x1024")

    args = parser.parse_args()

    raw_lox = args.loxodromes or ["0,0,45"]
    loxodromes_list = parse_loxodromes(raw_lox)

    if not loxodromes_list:
        print("Нет корректных локсодром. Выходим.")
        return

    globe_mesh = build_globe_mesh(args.texture, resize=(2048,1024) if args.highres else (360,180))
    fig = go.Figure()
    fig.add_trace(globe_mesh)

    line_colors = ["red", "blue", "green", "orange", "purple", "cyan", "magenta", "yellow"]

    for idx, (lat0, lon0, azimuth) in enumerate(loxodromes_list):
        x, y, z = loxodrome(lat0=lat0, lon0=lon0, azimuth_deg=azimuth,
                            steps=800, step_size=1)
        fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode="lines",
            line=dict(color=line_colors[idx % len(line_colors)], width=5),
            name=f"Локсодром {lat0},{lon0},{azimuth}"
        ))

    fig.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="data"
        ),
        title="Локсодромы на цветной сфере"
    )

    fig.write_html(args.output, auto_open=True)
    print(f"Готово! Файл сохранён: {args.output}")

if __name__ == "__main__":
    main()
