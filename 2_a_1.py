from binance.client import Client
import config

# Configurar la API key y secret key
client = Client(config.API_KEY, config.SECRET_KEY)

#obtiene informacion de las monedas de binance
exchange_info = client.futures_exchange_info()




#variables para el 2 a 1
symbol = input('digite la moneda, ejemplo(BTC)').upper() + "USDT"
long_o_short = int(input('long digita 1 short digita 0 '))
precio_entrada = float(input('digite precio entrada: '))
precio_stop = float(input('digite precio stop: '))
numero_recompras = 1
stop_loss_dolar = float(input('digite cuanto esta dispuesto a perder: '))
type = "LIMIT"
timeInForce = "GTC"
isIsolated = True

#recorre los simbolos
symbol_info = next((s for s in exchange_info['symbols'] if s['symbol'] == symbol), None)

if symbol_info is None:
    # El símbolo no se encuentra en Binance
    raise ValueError(f'El símbolo {symbol} no está disponible en Binance')

cantidad_decimales_precio = int(symbol_info['pricePrecision'])
cantidad_decimales_moneda = int(symbol_info['quantityPrecision'])

#variables calculadas a partir de las variables 2 a 1
if long_o_short == 1:
    porciento_distancia = ((precio_entrada - precio_stop)/precio_entrada)
    monto_posicion = stop_loss_dolar / porciento_distancia
    side = "BUY"
    positionSide = "LONG"
elif long_o_short == 0:
    porciento_distancia = ((precio_stop - precio_entrada)/precio_stop)
    monto_posicion = stop_loss_dolar / porciento_distancia
    side = "SELL"
    positionSide = "SHORT"

monto_posicion_monedas = monto_posicion / precio_entrada

if numero_recompras == 0:
    cantidad_compra_1 = monto_posicion_monedas
    precio_compra_1 = precio_entrada
    stop_loss_recompras = precio_stop
elif numero_recompras == 1:
        cantidad_compra_1 = monto_posicion_monedas / 2
        cantidad_compra_2 = cantidad_compra_1 + (cantidad_compra_1 * 0.4)
        costo_total = cantidad_compra_1 + cantidad_compra_2
        precio_compra_1 = precio_entrada
        precio_compra_2 = precio_stop
        if long_o_short == 1:
            stop_loss_recompras = (((precio_compra_1 * cantidad_compra_1) + (precio_compra_2 * cantidad_compra_2)) / costo_total) / (1 + (stop_loss_dolar/((precio_compra_1 * cantidad_compra_1) + (precio_compra_2 * cantidad_compra_2))))
        else:
            stop_loss_recompras = (((precio_compra_1 * cantidad_compra_1) + (precio_compra_2 * cantidad_compra_2)) / costo_total) * (1 + (stop_loss_dolar/((precio_compra_1 * cantidad_compra_1) + (precio_compra_2 * cantidad_compra_2))))

# Crear la orden en modo de cobertura
order = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=round(cantidad_compra_1,cantidad_decimales_moneda),
    price=round(precio_compra_1, cantidad_decimales_precio),
    positionSide=positionSide,
    isIsolated=isIsolated
)
print('order_1 OK')

# Crear la segunda orden en modo de cobertura
order_2 = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=round(cantidad_compra_2,cantidad_decimales_moneda),
    price=round(precio_compra_2,cantidad_decimales_precio),
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('order_2 OK')


# Definir los parámetros de la orden stop-loss
type = "STOP_MARKET"
closePosition = True



# Crear la orden stop-loss
stop_order = client.futures_create_order(
    symbol=symbol,
    side="SELL" if long_o_short == 1 else "BUY",
    type=type,
    stopPrice=round(stop_loss_recompras, cantidad_decimales_precio),
    closePosition=closePosition,
    positionSide="LONG" if long_o_short == 1 else "SHORT",
    isIsolated=isIsolated
)
print('stop-loss OK')