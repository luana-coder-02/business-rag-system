# Business RAG Chat System
Este proyecto es un sistema de **Generación Aumentada por Recuperación (RAG)** que utiliza un modelo de lenguaje grande (LLM) de **Ollama** para responder preguntas sobre analítica de datos, marketing digital y gestión de proyectos.
El sistema recupera información relevante de un conjunto de datos especializado para generar respuestas precisas y contextualizadas.
## 🎯 Resumen del Proyecto
El objetivo es ofrecer un recurso preciso y eficiente que responda a consultas específicas, sirviendo como una herramienta de apoyo en la toma de decisiones basada en información verificable.
El proyecto demuestra la capacidad de integrar un **LLM local** con una base de conocimiento externa, superando las limitaciones de la información pre-entrenada del modelo, **sin depender de servicios en la nube ni de una interfaz web**.
### ⚙️ Habilidades y Características Demostradas
- **Ejecución 100% local**: El sistema se corre directamente en la máquina del usuario sin necesidad de conexión externa.
- **Integración de LLM con Ollama**: Uso de modelos open-source como **Mistral** para generar respuestas.
- **Base de datos vectorial (ChromaDB)**: Implementación de un almacén persistente de embeddings para recuperación rápida y eficiente.
- **Gestión de estado de sesión**: Historial de conversación almacenado por usuario para mantener coherencia y contexto.
- **Persistencia de datos**: Sistema de logging en chat_log.jsonl para registrar las interacciones.
- **Organización del proyecto**: Uso de requirements.txt y una estructura modular clara para asegurar reproducibilidad y mantenimiento.
## 🛠️ Tecnologías del Stack
- Python 3.10+
- Ollama
- Mistral (modelo de lenguaje)
- ChromaDB
- Sentence Transformers
- Datasets (Hugging Face)
- JSON
## 🔮 Próximas Mejoras y Hoja de Ruta
Las siguientes funcionalidades están planificadas para futuras versiones, con el objetivo de hacer del sistema una herramienta aún más robusta y útil:
- **Evaluación automática de respuestas**: Calificación de precisión y relevancia.
- **Cambio de modelo desde configuración**: Opción de seleccionar diferentes modelos sin modificar el código base.
- **Exportar resultados**: Conversaciones o resultados exportables a CSV/JSON.
- **Filtros semánticos**: Filtrado de documentos por categorías o temas.
- **Pruebas unitarias**: Validación de componentes de forma aislada.
## 🤝 Contacto
Si tienes alguna pregunta sobre el proyecto, te interesa mi trabajo o quieres hablar sobre una oportunidad profesional, no dudes en contactarme.

**Luana Genes**

**Email**: genesluana275@gmail.com o luanagenes275@gmail.com
