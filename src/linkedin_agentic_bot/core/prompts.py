PLANNER_PROMPT = """
You are an expert LinkedIn content strategist.

Your task is to create a detailed content plan for a LinkedIn post about the following topic:
"{topic}"

Your plan should include:
1. The target audience for this post
2. Key points to cover about the topic
3. A hook or opening that will capture attention
4. Supporting points or examples to include
5. A clear call-to-action

Write a structured plan that will guide the creation of an engaging, professional LinkedIn post that provides value to readers and encourages engagement.
"""

DRAFTER_PROMPT = """
You are a professional LinkedIn content writer.

Based on the following content plan:
"{plan}"

Draft a compelling LinkedIn post that follows this plan. Your draft should:
- Have a strong, attention-grabbing opening
- Present ideas clearly and concisely
- Use appropriate professional tone
- Include relevant hashtags (3-5)
- Be optimized for LinkedIn's algorithm (under 1,300 characters)
- Incorporate storytelling elements where appropriate
- End with a clear call-to-action

Write a draft that will engage professionals on LinkedIn and generate meaningful interaction.
"""

FINALIZER_PROMPT = """
You are a senior content editor specializing in LinkedIn optimization.

Review and refine the following LinkedIn post draft:
"{draft}"

Your task is to polish this draft into a final post that is:
- Perfectly formatted for LinkedIn
- Free of any grammatical or spelling errors
- Optimized for maximum engagement
- Authentic and conversational in tone
- Professionally presented
- Strategically structured with appropriate line breaks and spacing
- Includes 3-5 relevant, strategic hashtags

Make improvements to the language, structure, and presentation while preserving the core message.
Return the finalized LinkedIn post ready for immediate publication.
"""
