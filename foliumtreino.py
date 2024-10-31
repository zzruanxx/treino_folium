import folium

# Criando o mapa centrado em um local específico (por exemplo, Rio de Janeiro, Brasil)
mapa = folium.Map(location=[-22.9068, -43.1729], zoom_start=12)

# Adicionando um marcador com pop-up e tooltip
folium.Marker(
    location=[-22.9068, -43.1729],
    popup="Rio de Janeiro - Pão de Açúcar",
    tooltip="Clique para mais informações",
    icon=folium.Icon(color="blue", icon="info-sign")
).add_to(mapa)

# Adicionando um círculo com raio específico para representar uma área
folium.Circle(
    location=[-22.9519, -43.2105],
    radius=500,  # em metros
    color="green",
    fill=True,
    fill_color="lightgreen",
    popup="Cristo Redentor - Área ao Redor"
).add_to(mapa)

# Adicionando uma camada de polígonos (por exemplo, uma área específica da cidade)
folium.Polygon(
    locations=[
        [-22.9106, -43.2045],
        [-22.9140, -43.1899],
        [-22.9227, -43.1925],
        [-22.9194, -43.2073]
    ],
    color="purple",
    fill=True,
    fill_color="purple",
    fill_opacity=0.3,
    popup="Área Especial do Parque"
).add_to(mapa)

# Adicionando camadas extras como satélite ou terreno (utilizando plugins de camadas do Folium)
folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Stamen Toner').add_to(mapa)
folium.LayerControl().add_to(mapa)  # Controle para alternar entre camadas

# Salvando o mapa como arquivo HTML
mapa.save("mapa_interativo.html")
