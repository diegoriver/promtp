# Prueba Técnica: Ingeniero Prompt - Tuya

## Descripción

Este repositorio contiene la implementación de código para la resolución de la prueba técnica para el rol de Ingeniero Prompt en Tuya. El sistema está diseñado como un bot multiagente modular que aborda las diferentes preguntas de la prueba.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

-   **/agents**: Contiene las clases de Python que representan a cada agente lógico (ej., agente de facturación, agente de casos complejos).
-   **/prompts**: Almacena las plantillas de prompts en archivos `.txt` y `.xml`. Separar los prompts del código permite una fácil iteración y mantenimiento.
-   **main.py**: Es el punto de entrada de la aplicación. Contiene el orquestador que dirige las solicitudes al agente correspondiente y un bucle principal para la interacción.

## Preguntas Implementadas por el Código

-   **Pregunta 6 y 7**: La lógica para el agente de facturación y el sistema RAG (simulado) está implementada en `agents/billing_agent.py` usando el prompt `prompts/pt06_billing_agent_template.xml`.
-   **Pregunta 8**: Se compara la implementación con y sin Chain-of-Thought (CoT) para explicar un cargo. Los prompts están en `prompts/pt08_...` y la lógica en `agents/complex_case_agent.py`.
-   **Pregunta 11**: Se incluye un prompt de auto-evaluación en `prompts/pt11_self_evaluation_template.txt` y una clase agente para simular su ejecución en `agents/code_eval_agent.py`.
-   **Pregunta 12**: El diseño general del proyecto responde a esta pregunta, utilizando clases de agente, estructuras de control, manejo de errores y código documentado y limpio.

## Cómo Ejecutar

1.  Clonar el repositorio:
    ```bash
    git clone [TU_URL_DE_GITHUB]
    cd tuya-prompt-test
    ```
2.  (Opcional) Crear un entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```
3.  Instalar dependencias (ej. si se usara una librería de LLM):
    ```bash
    pip install -r requirements.txt
    ```
4.  Ejecutar el script principal:
    ```bash
    python main.py
    ```
