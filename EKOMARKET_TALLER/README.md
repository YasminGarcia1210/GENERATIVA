# 🛍️ EcoMarket - Sistema de Consulta de Pedidos

Este proyecto implementa un chatbot inteligente para el servicio al cliente de EcoMarket, permitiendo consultas sobre el estado de pedidos utilizando procesamiento de lenguaje natural.

## 🚀 Características

- Consulta de estado de pedidos en tiempo real
- Respuestas personalizadas y empáticas
- Manejo de diferentes estados de pedidos (en tránsito, entregado, retrasado, etc.)
- Enlaces de rastreo automáticos
- Interfaz de línea de comandos amigable

## 📋 Requisitos

- Python 3.x
- Transformers
- PyTorch
- Un archivo `pedidos.txt` con la base de datos de pedidos

## 🛠️ Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/YasminGarcia1210/TAREAS.git
cd TAREAS
```

2. Instala las dependencias:
```bash
pip install transformers torch
```

## 💻 Uso

1. Ejecuta el programa:
```bash
python main.py
```

2. Realiza consultas sobre pedidos, por ejemplo:
   - "¿Cuál es el estado del pedido 1001?"
   - "¿Cuándo llegará mi pedido 1004?"
   - "¿Por qué se retrasó el pedido 1003?"

3. Para salir, escribe 'salir'

## 📝 Formato del Archivo de Pedidos

El archivo `pedidos.txt` debe contener la información de los pedidos en el siguiente formato:
```
Pedido [número] - Estado: [estado] - [información adicional]
```

Ejemplo:
```
Pedido 1001 - Estado: En tránsito - Fecha estimada de entrega: 2025-10-01
Pedido 1002 - Estado: Entregado - Fecha de entrega: 2025-09-25
```

## 👥 Autores

- Yasmín García

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE.md](LICENSE.md) para detalles