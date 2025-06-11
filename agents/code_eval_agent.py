"""
agents/code_eval_agent.py
Agente para la autoevaluación del uso de IA generativa.
Implementación para la pregunta 11.
"""
import os

class CodeEvalAgent:
    """Un agente diseñado para autoevaluar la implementación de la prueba."""
    def __init__(self):
        print("(Agente de Evaluación de Código listo)")
        # Carga la plantilla desde el archivo
        with open("prompts/pt11_self_evaluation_template.txt", "r") as f:
            self.eval_template = f.read()
            
    def _get_project_code(self):
        # Esta funcion lee todos los archivos .py para inyectarlos en el prompt
        code_str = ""
        for root, _, files in os.walk("."):
            for file in files:
                if file.endswith(".py"):
                    with open(os.path.join(root, file), 'r') as f:
                        code_str += f"--- Contenido de {file} ---\n"
                        code_str += f.read()
                        code_str += "\n\n"
        return code_str

    def run(self):
        project_code = self._get_project_code()
        
        final_prompt = self.eval_template.format(
            codigo_del_repositorio=project_code,
            respuestas_prueba_tecnica="El candidato envió las respuestas en un documento separado."
        )

        print("\n--- PROMPT DE AUTO-EVALUACIÓN (P11) ---")
        print(final_prompt)
        print("--- FIN DEL PROMPT ---")
        return "El prompt de autoevaluación está listo para ser enviado a un LLM."


# Esto permite correr y probar este agente de manera aislada
if __name__ == "__main__":
    eval_agent = CodeEvalAgent()
    eval_agent.run()

