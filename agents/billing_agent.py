"""
agents/billing_agent.py

Agente especializado en responder preguntas generales de facturación.
Correspondiente a la implementación de la pregunta 6.

Características:
- Carga una plantilla de prompt desde un archivo .xml.
- Estructurado como una clase modular.
- Incluye comentarios y nombres de variable descriptivos.
"""

class BillingAgent:
    """
    Agente para respuestas de facturación basadas en un ROL estricto.
    Usa el prompt de la pregunta 6.
    """
    def __init__(self):
        """Inicializa el agente cargando la plantilla del prompt."""
        # Se explica el rol del agente en este comentario.
        print("(Agente de Facturación listo)")
        try:
            # Cargar el prompt desde el archivo ayuda a separar lógica y datos
            with open("prompts/pt06_billing_agent_template.xml", "r") as f:
                self.prompt_template = f.read()
        except FileNotFoundError:
            # Manejo básico de error
            self.prompt_template = "ERROR: No se encontró la plantilla de prompt."
            print(f"[ERROR_BillingAgent]: El archivo de prompt no fue encontrado.")
            
    def _build_prompt(self, context, question):
        """Construye el prompt final reemplazando las variables."""
        return self.prompt_template.format(
            texto_de_los_chunks_del_extracto_recuperados_via_rag=context,
            pregunta_del_cliente=question
        )
        
    def run(self, context, question):
        """
        Ejecuta el agente. En una aplicación real, haría la llamada al LLM.
        Aquí, simulamos el proceso imprimiendo el prompt consolidado.
        """
        # Nombres descriptivos para las variables.
        final_prompt = self._build_prompt(context, question)
        print("\n--- PROMPT ENVIADO AL LLM ---
        ")
        print(final_prompt)
        print("--- FIN DEL PROMPT ---")
        
        # En una aplicación real, aquí iría la llamada al LLM
        # response = llm_client.generate(final_prompt)
        # return response
        
        # Para esta prueba, devolvemos una respuesta simulada.
        return "He recibido tu pregunta y la estoy procesando con base en las reglas establecidas."
