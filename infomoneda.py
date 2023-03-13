from binance.client import Client
import config

# Configurar la API key y secret key
client = Client(config.API_KEY, config.SECRET_KEY)

symbol = input('Digita la moneda ejemplo:(BTCUSDT)==> ')

# Obtener información de todas las posiciones abiertas
positions = client.futures_position_information()

# Obtener información sobre el símbolo
symbol_info = client.futures_exchange_info()["symbols"]
for s in symbol_info:
    if s["symbol"] == symbol:
        precision = s["pricePrecision"]
        break

# Filtrar la información para encontrar la posición deseada
for position in positions:
    if position["symbol"] == symbol:
        qty = float(position["positionAmt"])
        price = float(position["entryPrice"])
        formatted_price = f"{price:.{precision}f}"
        print(f"Posición abierta en {symbol}: {qty} monedas a un precio de entrada de {formatted_price}")
