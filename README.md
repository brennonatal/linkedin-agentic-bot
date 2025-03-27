# LinkedIn Agentic Bot

A simple implementation of an agentic workflow for LinkedIn post content generation.

## Overview

This project demonstrates how a multi-agent workflow can generate high-quality LinkedIn content from a simple topic input. The workflow leverages a series of specialized agents, each with a specific role in the content creation process.

## How It Works

The workflow follows a sequential process:

1. **Topic Input**: The user provides a topic (e.g., "Artificial Intelligence", "Remote Work", "Digital Marketing")

2. **Planning Phase**: The Planner agent creates a structured content plan including:
   - Target audience
   - Key points to cover
   - Hook/opening
   - Supporting points
   - Call-to-action

3. **Drafting Phase**: The Drafter agent takes the plan and creates a compelling LinkedIn post draft with:
   - Attention-grabbing opening
   - Clear, concise content
   - Professional tone
   - Relevant hashtags
   - Call-to-action

4. **Finalization Phase**: The Finalizer agent polishes the draft into a publication-ready post with:
   - Perfect formatting
   - Grammar correction
   - Engagement optimization
   - Strategic structure
   - Relevant hashtags

## Usage

To use the LinkedIn Post Generator:

1. Clone this repository
2. Install dependencies with `uv`:
   ```
   uv sync
   ```
   Or with pip:
   ```
   pip install -e .
   ```
3. Run the main script:
   ```
   python main.py
   ```
4. Enter your desired topic when prompted
5. For debugging with detailed execution logs:
   ```
   python main.py --debug
   ```

## Technical Implementation

The workflow is built using:
- LangGraph for implementing the agent workflow
- LangChain for creating the agent chains
- Ollama for local LLM inference
- Pydantic for state management

## Future Implementation Ideas

### Internet Search Integration
- [ ] Add real-time web search capabilities to enrich content with current trends, statistics, and expert opinions
- [ ] Incorporate relevant news and industry updates automatically
- [ ] Enable citation of sources for more authoritative content

### Automated Topic Selection
- [ ] Implement trending topic detection based on industry or interests
- [ ] Add scheduling capabilities for regular content generation
- [ ] Create topic suggestion features based on profile information and past engagement

### Enhanced Personalization
- [ ] Add company/user profile integration to align with brand voice
- [ ] Enable customization of content type (thought leadership, case study, how-to)
- [ ] Implement audience-specific content adjustments

### Analytics and Feedback Loop
- [ ] Track performance of generated posts
- [ ] Incorporate feedback to improve future content
- [ ] Develop learning mechanisms to adapt to engagement patterns

### Long-Term Memory
- [ ] Implement storage of previously generated posts to avoid repetition
- [ ] Add content history analysis to diversify topics and styles
- [ ] Create a content calendar feature that ensures variety
- [ ] Develop post similarity detection to prevent unintentional duplication