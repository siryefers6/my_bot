from binance.client import Client
import config
import decimal

# Configurar la API key y secret key
client = Client(config.API_KEY, config.SECRET_KEY)


#variables para el 2 a 1

long_o_short = int(input('long digita 1 short digita 0 '))
precio_entrada = float(input('digite precio mayor: '))
precio_stop = float(input('digite precio menor: '))
numero_recompras = int(input('digite numero de recompras: '))
stop_loss_dolar = float(input('digite cuanto esta dispuesto a perder: '))


#variables calculadas a partir de las variables 2 a 1

porciento_distancia = ((precio_entrada - precio_stop)/precio_stop)
monto_posicion = stop_loss_dolar / porciento_distancia

#cantidad de la posicion en monedas
if long_o_short == 1:
    monto_posicion_monedas = monto_posicion / precio_entrada
else:
    monto_posicion_monedas = monto_posicion / precio_stop




print(porciento_distancia)
print(monto_posicion)
print(monto_posicion_monedas)




'''
# Definir los parámetros de la orden
symbol = "XRPUSDT"
side = "BUY"
type = "LIMIT"
timeInForce = "GTC"
quantity = 13.6
price = 0.3687
positionSide = "LONG" # o "SHORT" dependiendo de su estrategia
isIsolated = True
quitar_orden = 1

# Crear la orden en modo de cobertura
if quitar_orden == 0:      
    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=type,
        timeInForce=timeInForce,
        quantity=quantity,
        price=price,
        positionSide=positionSide,
        isIsolated=isIsolated
    )
    print('order_1 OK')

# Definir los parámetros de la segunda orden
decimals_2 = -decimal.Decimal(str(quantity)).as_tuple().exponent
quantity_2 = round(quantity * 2, decimals_2)
decimals = -decimal.Decimal(str(price)).as_tuple().exponent
price_2 = round(price * (1 - 0.03), decimals)

# Crear la segunda orden en modo de cobertura
order_2 = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=quantity_2,
    price=price_2,
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('order_2 OK')

# Definir los parámetros de la tersera orden
quantity_3 = round(quantity_2 * 2, decimals_2)
decimals = -decimal.Decimal(str(price)).as_tuple().exponent
decimals_2 = -decimal.Decimal(str(quantity)).as_tuple().exponent
price_3 = round(price_2 * (1 - 0.03), decimals)

# Crear la tersera orden en modo de cobertura
order_3 = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=quantity_3,
    price=price_3,
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('order_3 OK')

# Definir los parámetros de la cuarta orden
quantity_4 = round(quantity_3 * 2, decimals_2)
decimals = -decimal.Decimal(str(price)).as_tuple().exponent
decimals_2 = -decimal.Decimal(str(quantity)).as_tuple().exponent
price_4 = round(price_3 * (1 - 0.03), decimals)

# Crear la cuarta orden en modo de cobertura
order_4 = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=quantity_4,
    price=price_4,
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('order_4 OK')

# Definir los parámetros de la quinta orden
quantity_5 = round(quantity_4 * 2, decimals_2)
decimals = -decimal.Decimal(str(price)).as_tuple().exponent
decimals_2 = -decimal.Decimal(str(quantity)).as_tuple().exponent
price_5 = round(price_4 * (1 - 0.03), decimals)

# Crear la quinta orden en modo de cobertura
order_5 = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=quantity_5,
    price=price_5,
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('order_5 OK')

# Definir los parámetros de la sexta orden
quantity_6 = round(quantity_5 * 2, decimals_2)
decimals = -decimal.Decimal(str(price)).as_tuple().exponent
decimals_2 = -decimal.Decimal(str(quantity)).as_tuple().exponent
price_6 = round(price_5 * (1 - 0.03), decimals)

# Crear la sexta orden en modo de cobertura
order_6 = client.futures_create_order(
    symbol=symbol,
    side=side,
    type=type,
    timeInForce=timeInForce,
    quantity=quantity_6,
    price=price_6,
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('order_6 OK')

total_quantity = round(quantity + quantity_2 + quantity_3 + quantity_4 + quantity_5 + quantity_6, decimals_2)

stop_price = round(price_6 * 0.99, decimals)

stop_order = client.futures_create_order(
    symbol=symbol,
    side="SELL",
    type="STOP_MARKET",
    quantity=total_quantity,
    stopPrice=stop_price,
    positionSide=positionSide,
    isIsolated=isIsolated
)

print('stop_order OK')
'''