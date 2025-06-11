"""
agents/complex_case_agent.py

Agente para manejar casos de cargos no reconocidos. Implementa una 
comparativa entre el uso y no uso de Chain-of-Thought (CoT).
Correspondiente a la pregunta 8.
"""

class ComplexCaseAgent:
    """Un agente que puede usar CoT para razonar sobre problemas."""
    def __init__(self):
        """Carga las plantillas de prompts de CoT y no-CoT."""
        print("(Agente de Casos Complejos listo)")
        self.no_cot_template = self._load_template("prompts/pt08_complex_case_no_cot_template.txt")
        self.with_cot_template = self._load_template("prompts/pt08_complex_case_with_cot_template.txt")

    def _load_template(self, file_path):
        """Función auxiliar para cargar plantillas."""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"[ERROR_ComplexAgent]: El archivo de prompt {file_path} no fue encontrado.")
            return "ERROR: Plantilla no encontrada."

    def run(self, context, question, use_cot=True):
        """ Ejecuta el agente con o sin la lógica de CoT. """
        template = self.with_cot_template if use_cot else self.no_cot_template
        
        # El nombre del cargo se debe extraer de la pregunta del usuario. Aquí lo simulamos.
        # En un sistema real se debería usar regex o un LLM para extraer la entidad.
        charge_name = "SEGUROS BOLIVAR S.A."
        
        final_prompt = template.format(
            contexto_extracto=context,
            nombre_cargo=charge_name,
            pregunta_cliente=question
        )
        
        print("\n--- PROMPT ENVIADO AL LLM C/S CoT ---")
        print(final_prompt)
        print("--- FIN DEL PROMPT ---")
        
        return "El prompt para este caso ha sido generado y mostrado en consola."
