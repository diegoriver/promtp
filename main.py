"""
main.py
Punto de entrada y orquestador del bot multiagente Tuya.
Responde al punto 12 de la prueba técnica.

Funcionalidad:
- Inicializa los agentes.
- Simula un bucle de interacción con el usuario.
- Utiliza estructuras de control (condicionales) para enrutar la 
  pregunta del usuario al agente correcto.
- Demuestra un uso modular y buenas prácticas de código.
"""
from agents.billing_agent import BillingAgent
from agents.complex_case_agent import ComplexCaseAgent
from agents.code_eval_agent import CodeEvalAgent

def orchestrator(user_question, context_data):
    """
    Función modular que actúa como un enrutador (router).
    Decide qué agente debe manejar la solicitud del usuario.
    """
    # En un sistema real, este enrutamiento podría ser una 
    # clasificacion hecha por un LLM más pequeño y rápido.
    if "no reconozco" in user_question.lower() or "cargo no reconocido" in user_question.lower():
        print("[Orquestador]: Redirigiendo a Agente de Casos Complejos...")
        complex_agent = ComplexCaseAgent()
        
        # Para la P8, comparamos CoT vs. no-CoT
        print("\n--- Respuesta SIN Chain-of-Thought ---")
        response_no_cot = complex_agent.run(context_data, user_question, use_cot=False)
        print(response_no_cot)
        
        print("\n--- Respuesta CON Chain-of-Thought ---")
        response_with_cot = complex_agent.run(context_data, user_question, use_cot=True)
        print(response_with_cot)
        
        return "Las respuestas con y sin CoT se han mostrado arriba."
        
    else: # Por defecto, va al agente de facturación general.
        print("[Orquestador]: Redirigiendo a Agente de Facturación...")
        billing_agent = BillingAgent()
        response = billing_agent.run(context_data, user_question)
        return response


if __name__ == "__main__":
    # Contexto simulado para la prueba (simulando una salida de RAG)
    simulated_context = """
    DETALLE DE TRANSACCIONES:
    - Fecha: 2023-11-05 | Descripción: COMPRA TIENDA ABC SAS | Monto: $50.00
    - Fecha: 2023-11-08 | Descripción: SEGUROS BOLIVAR S.A. | Monto: $15.00
    - Fecha: 2023-11-12 | Descripción: AVANCE EN CAJERO BANCO X | Monto: $100.00
    """
    
    # Bucle de interacción principal, como solicita el punto 12.b
    print("Iniciando Bot Multiagente de Soporte Tuya...")
    print("Escribe 'salir' para terminar.")
    
    while True:
        try:
            # Líneas < 80 caracteres
            user_input = input("\n[Tú]: ")
            
            if user_input.lower() == "salir":
                print("[Bot]: ¡Gracias por usar nuestro servicio!")
                break
            
            # Flujo de ejecución principal
            bot_response = orchestrator(user_input, simulated_context)
            print(f"\n[Asistente Tuya]: {bot_response}")

        # Manejo básico de errores como solicita el punto 12.c
        except Exception as e:
            print(f"[ERROR]: Ha ocurrido un error inesperado: {e}")

