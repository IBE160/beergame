# Technical Research Report: Python LLM Orchestration Library

**Report Date:** 2025-10-27
**Author:** Mary, Business Analyst

## 1. Executive Summary

This report evaluates four leading Python libraries for orchestrating Large Language Model (LLM) interactions for a new greenfield proof-of-concept application. The goal is to select a library for developing AI players for a game, requiring provider-agnosticism (initially Gemini 2.5 Pro) and reliable, structured JSON output for game moves.

After a detailed comparative analysis, **Pydantic AI is the primary recommendation**. It is a modern, focused framework built by the Pydantic team that directly solves the core challenge of obtaining type-safe, validated data from LLMs in a model-agnostic way. It hits the perfect "sweet spot" of providing powerful functionality without the cognitive overhead of a larger, more complex framework.

**Haystack** is a strong second choice, offering a more mature, pipeline-centric approach that may be suitable if the project's scope expands to include complex data retrieval (RAG) tasks.

## 2. Research Goal & Requirements

The primary goal is to select a Python library that simplifies interaction with LLMs like Gemini 2.5 Pro, while ensuring the flexibility to switch providers in the future. The library must provide significant functionality to aid in prompt and context engineering, specifically for generating structured JSON output.

### 2.1. Functional Requirements
- Must support Gemini 2.5 Pro/Flash.
- Must be provider-agnostic, allowing for easy switching to other models.
- Must reliably produce structured JSON output conforming to a predefined schema.
- Must provide robust error handling and retry mechanisms.
- Streaming responses are a "nice-to-have" for observing the AI's reasoning.

### 2.2. Non-Functional Requirements
- **Developer Experience**: The library should be intuitive, well-documented, and not overly complex.
- **Performance**: A response time of a few seconds per AI move is acceptable.
- **Scalability**: Must support at least 4 simultaneous AI players.

### 2.3. Constraints
- **Language**: Python
- **Cost**: Open-source or free-tier friendly.
- **Project Type**: Greenfield, Proof-of-Concept.

## 3. Technology Options Evaluated

1.  **Haystack**: A composable, data-centric framework for building LLM applications with a focus on pipelines.
2.  **Semantic Kernel**: A lightweight, goal-oriented orchestration library from Microsoft that focuses on integrating LLMs with native code via "skills".
3.  **DSPy**: A novel "programming model" from Stanford that compiles Pythonic logic into optimized prompts for specific LLMs.
4.  **Pydantic AI**: A new, focused framework from the Pydantic team for building production-grade, type-safe AI applications.

## 4. Comparative Analysis

| Feature / Requirement | Haystack | Semantic Kernel | DSPy | Pydantic AI |
| :--- | :--- | :--- | :--- | :--- |
| **Provider Agnostic** | ✅ **Excellent**. Mature integrations for most providers (Hugging Face, OpenAI, Cohere, Google Vertex AI). Switching is straightforward. | ✅ **Very Good**. Uses a "Connector" model. Supports OpenAI, Azure, Hugging Face, and others. Well-designed for interoperability. | ✅ **Very Good**. Designed to be model-agnostic. You configure the LLM once, and the compiler targets it. Supports all major providers. | ✅ **Excellent**. This is a core design principle. It is model-agnostic and supports a wide range of providers out of the box. |
| **Structured Output** | ✅ **Good**. Can output JSON and has components to validate it, but it's not the primary focus. Requires more manual setup compared to others. | ✅ **Good**. Can use "function calling" to get structured data. Requires defining functions and parsing the results. Less direct than Pydantic-native solutions. | ✅ **Very Good**. Uses typed signatures (`dspy.TypedPredictor`) to guide the model. The compiler optimizes prompts to produce the desired type. Very powerful but a novel concept. | ✅ **Best-in-Class**. This is its main purpose. You define a Pydantic model, and the library guarantees the LLM output will conform to it. Simple, direct, and robust. |
| **Prompt Engineering** | ✅ **Very Good**. `PromptBuilder` is a powerful and explicit tool for creating and managing complex prompts with variables and logic. | ✅ **Good**. Prompts are managed as part of "Skills". It's a clean concept but can feel abstract if you just want to manage a single, complex prompt. | ✅ **Revolutionary**. You don't write the final prompt. You write the logic, and DSPy's compiler writes the prompt *for you*. The highest level of abstraction. | ✅ **Very Good**. Manages prompts in a clear, Pythonic way. Its main strength is automatically adding the necessary instructions to get the structured output you defined. |
| **Developer Experience** | ✅ **Good**. The "Pipeline" concept is intuitive and visual. Can feel a bit verbose for simple tasks. Mature with extensive documentation. | ✅ **Good**. Well-documented with Microsoft's backing. The concepts of "Skills" and "Planners" can have a learning curve. | ⚠️ **Mixed**. A higher initial learning curve due to its unique concepts (compilation, optimizers). Extremely powerful once grasped, but less intuitive at the start. | ✅ **Excellent**. For anyone familiar with Pydantic, the experience is incredibly intuitive. The code is clean, Pythonic, and directly solves the problem with minimal boilerplate. |
| **Use Case Fit** | A solid choice. It can definitely solve the problem, but might be slight overkill if you don't need its advanced data retrieval (RAG) features. | A viable choice, but its agent/skill orchestration focus is more than you need for a single LLM call to get a game move. | A very powerful choice, but its novel compilation approach might slow down initial PoC development. Better for optimizing a working prototype than building the first version. | **A perfect fit**. It is designed for exactly this task: making a single, reliable, structured call to an LLM and getting a validated data object back. |

## 5. Recommendations and Decision

### 5.1. Primary Recommendation: Pydantic AI

**Pydantic AI is the clear winner for this project.** It aligns perfectly with all stated requirements and constraints.

*   **Solves the Core Problem Directly**: Its entire purpose is to provide reliable, structured output from LLMs using Pydantic models, which was identified as a critical need.
*   **Excellent Developer Experience**: The API is clean, Pythonic, and will feel natural, reducing the learning curve and speeding up PoC development.
*   **Future-Proof and Flexible**: Being model-agnostic and built by the trusted Pydantic team ensures it will stay current and well-maintained. It provides the power you need without forcing you into a complex framework you don't.

### 5.2. Alternative Option: Haystack

If the project were expected to quickly evolve beyond simple LLM calls into a more complex system that needs to retrieve information from documents or databases to inform the AI players' decisions (Retrieval Augmented Generation), then **Haystack** would be a superior choice. Its pipeline-centric model excels at these data-intensive RAG workflows. For the current scope, it is a solid but slightly less direct solution than Pydantic AI.

## 6. Next Steps

1.  **Install Pydantic AI**: Begin by installing the library (`pip install pydantic-ai`).
2.  **Prototype**: Develop a small prototype that:
    a. Defines the `GameOrder` using a Pydantic model.
    b. Uses `PydanticAI` to call the Gemini 2.5 Pro model with a sample game state.
    c. Verifies that the output is a validated `GameOrder` object.
3.  **Integrate**: Integrate the prototype into the main game application loop.
