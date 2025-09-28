from transformers import pipeline

def main():
    print("\n🌟 Sistema de Consultas EcoMarket 🌟")

    chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

    pedidos = """
    Pedido 1001 - Entregado el 21/09
    Pedido 1002 - Retrasado, nueva fecha 28/09
    Pedido 1003 - En camino, entrega prevista 25/09
    """

    while True:
        consulta = input("👤 Tu consulta: ").strip()
        if consulta.lower() == "salir":
            break

        # Prompt mejorado
        prompt = f"""
        Actúa como un agente de soporte de EcoMarket.
        Base de datos de pedidos:
        {pedidos}

        Pregunta: {consulta}
        Responde SOLO con el estado del pedido y un mensaje empático.
        """

        # Aquí aplicamos el filtro
        respuesta = chatbot(prompt, max_new_tokens=80)[0]["generated_text"]

        # Si el modelo repite el prompt, cortamos después de "Pregunta:"
        if "Pregunta:" in respuesta:
            respuesta = respuesta.split("Pregunta:")[-1].strip()

        print("\n💬 Respuesta:\n", respuesta)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()

