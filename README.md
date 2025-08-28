# Commercial RAG Chat System
Este proyecto es un sistema de **Generación Aumentada por Recuperación (RAG)** que utiliza un modelo de lenguaje grande (LLM) de Ollama para responder preguntas sobre analítica de datos, marketing digital y gestión de proyectos. El sistema recupera información relevante de un conjunto de datos especializado para generar respuestas precisas y contextualizadas.
## 🎯 Resumen del Proyecto
El objetivo es ofrecer un recurso preciso y eficiente que responda a consultas específicas, sirviendo como una herramienta de apoyo en la toma de decisiones basada en información verificable. El proyecto demuestra la capacidad de integrar un **LLM** local con una **base de conocimiento externa** para superar las limitaciones de la información pre-entrenada del modelo.
### ⚙️ Habilidades y Características Demostradas
- **Desarrollo y Despliegue de Aplicaciones Web**: Creación de una aplicación interactiva con **Streamlit** que puede ejecutarse localmente o ser desplegada para su uso.
- **Integración de LLM**: Utilización del modelo de lenguaje **Mistral a través de Ollama**, mostrando familiaridad con la integración de modelos de IA de código abierto.
- **Vector Database (ChromaDB)**: Implementación de una base de datos vectorial persistente para almacenar y gestionar embeddings de documentos, permitiendo una recuperación de información rápida y eficiente.
- **Gestión de Estado de Sesión**: Manejo del historial de conversación por usuario para mantener la coherencia y el contexto en las interacciones.
- **Persistencia de Datos**: Desarrollo de un sistema de logging para registrar las interacciones en un archivo ***chat_log.jsonl***, lo que permite un seguimiento y análisis.
- **Organización del Proyecto**: Uso de ***requirements.txt*** y una estructura de código clara para asegurar la reproducibilidad y el mantenimiento.
## 🛠️ Tecnologías del Stack
- Python 3.10+
- Streamlit
- Ollama
- Mistral (modelo de lenguaje)
- ChromaDB
- Sentence Transformers
- Datasets (Hugging Face)
- JSON
