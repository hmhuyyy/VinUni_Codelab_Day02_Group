# Phase 6 — AI Log & Reflection

> Draft reflection based on my work on this lab. I will personalize it before submitting, especially any details that do not match my own experience.

## How I used AI

I used AI as a brainstorming partner to list possible operational problems and turn one of them into a problem statement, workflow, metrics, and a prompt prototype. It helped me organize the work into actors, steps, bottlenecks, boundaries, and test cases. The most useful part was asking it to challenge whether an LLM was actually needed and where a human should remain in control.

## Where I had to verify or correct it

Early suggestions included specific figures such as minutes per case and cancellation percentages without evidence from company data. I treated those as unverified, removed unsupported baseline claims, and marked remaining targets as hypotheses to measure. I also noticed that an initial Xanh SM pickup-point idea did not match the battery/mobile-charger scenario in the starter code. I aligned the selected problem with the prototype and changed the architecture to use deterministic rules for the battery and distance limits, with an LLM only drafting an explanation.

The first run also showed that the starter file had not yet implemented the API call. After implementing it, I encountered an API-version error; changing the Gemini client to `v1beta` resolved that error. The two adversarial tests I ran then passed. This showed me that successful output on a couple of examples is useful evidence, but not proof that a prompt is safe or ready for production.

## What I changed because of that

- Marked operational workflow details, time estimates, and impact figures as assumptions until they can be checked with operators and logs.
- Kept `[DRAFT_ONLY]` on every response and made clear that a proposed dispatch is not an executed dispatch.
- Put the battery threshold and maximum station distance in deterministic rules rather than relying on the LLM to calculate safety.
- Added a missing-telemetry/prompt-injection test and made failed checks return a non-zero process status. I still need to run that added test with a valid API key.
- Kept a human approval step and manual fallback in the proposed workflow.

## Reflection

AI helped me move from a broad idea to a testable prototype quickly, but it also made plausible-sounding assumptions easy to mistake for facts. I need to check claims against real evidence, use rules for strict safety constraints, and treat model output as a draft. Before recommending deployment, I would validate the workflow with the people who do the work, test representative and adversarial cases, and measure performance against a real baseline.
