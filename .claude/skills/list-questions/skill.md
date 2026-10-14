---
name: list-questions
description: Compose a list of questions that need answering in order to create a proper, made-to-measure proposal as a response to an RFP or RFI request from a prospect. Ask whether there is an existing platform available which can be inventorized to compare with the project briefing resulting in relevant questions.
---

Depending on the `input/`-folder, determine whether the request is about a content website/platform or an e-commerce platform (product pages, customer regsitration, online payment). Only list questions which are relevant for this project request.
Use the below topics and example questions as inspiration to compose a list of questions which are not answered from information available in the `input/`-folder documentation. The below example questions are not necessarily related to the context of the project, so double-check if they are relevant. Feel free to add additional questions per topic when they are relevant. The example questions below are not a conclusive list.
List a maximum of 10 to 15 questions per topic, prioritize the most relevant ones which would impact the scope of the project.
Any questions you com eup with but that are answered from the documentation in `input/`-folder need to be listed in a final section for our internal reference.

## Strategy & business context

Aim for questions clarifying the business context and strategic vision of the prospect.

### Example questions

- Can you share the full persona list and their primary journeys? What does each persona need to do on the site vs. just read? Do you have any research data available that you can share regarding top tasks etc? 

- How will you measure whether the new website is successful 6 months after launch? Are there specific KPIs (lead volume, organic traffic, conversion rate, ...)? 

- Which other (relevant) digital transformation tracks will take place within the organisation? 

- What are the biggest frustrations end users and editors experience with the current platform today? 

- Could you give us some background on the different roles & responsibilities within the marketing team? Beyond the named project team, how many people will be editing content, and in which markets? 

- What are the main dependencies and risks you see for this project to become a success?

## Multi-site, languages & Localisation

Aim for questions clarifying if there is only a need for single frontend touchpoint, or multiple (multi-site). Clarify the number of required languages or locales in order to be able to list clear requirements on localisation so we can take this into account when performing a CMS platform selection.

### Example questions

- Which languages and locales will go live on day one? Are any markets post-launch scope? 

- Does content differ structurally between languages/markets, or is the same content available for all languages/markets, only translated?

- Do you have an existing translation memory (TM), glossary, or preferred TMS (e.g. Phrase, Lokalise)? Or should we propose translation tooling as part of the CMS setup? 

## Content & migration

Aim for questions clarifying what the content within the project consists of: content types (content page, news item, event item, FAQ, ...). If you detect any additional interactive components like a dealer locator, calculators or similar tools, ask how these are managed or where the data comes from.

### Example questions

- How many pages currently exist across all languages? How many articles/blog posts? Do you have access to analytics showing which pages receive the most traffic?

- Which types of content exist on the website? (e.g. pure content pages, event items, news or blog items, FAQ, ...)

- Is all content publicly available or should some content be gated? (only available after authentication)

- Should we include content migration in this scope? Is there a content freeze period planned before cutover? 

- What is the current URL structure, and do you have a preferred structure for the new site? Should we include a full crawl, redirect mapping, and post-launch redirect monitoring? 

## Search

Aim for questions clarifying the ideal search requirements.

### Example questions

- Which content needs to be exposed though search? Content-only or other data like dealer information, products (if relevant) as well?

- Are you open to using best-of-breed platforms for a capability like search? (e.g. Algolia)

## User/Customer identity management

Aim for questions clarifying if user or customer registration is required and where their data should be stored.

### Example questions

- Is registration and authentication required? Where should credentials be stored? (e.g. locally or using an IAM platform like Azure Entra ID?)

- Is multi-account support required? (e.g. a single customer can have multiple accounts available)

## Platform & Technology

Aim for questions clarifying requirements on platforms and technology.

### Example questions

- For the platform, do you have a preference for SaaS, PaaS or self-hosted?

- Is there an architecture design that you prefer (e.g. monolith vs composable architecture)? What are the main reasons that architecture design type stands out for you?

- Do you have a preference for open source, or are there specific reasons you'd steer away from it? 

- Do you have a preferred (headless) CMS or a shortlist in mind? Any platforms explicitly ruled out? 

- How many content editors are actively working within the team? How may users would you need in the 

- Which hosting platform (private cloud, public cloud, on-prem, ...) is preferred? Is providing a hosting solution part of the scope of this project?

- Which platforms need to be integrated with? Are these platforms already up and running or do they still need to be set up? Is there additional information available on which versions of these platforms are used?

- Is there an overview available of which platforms are defined as the Systems-of-Record for different types of content?

- Technology preference: is there a preference of frontend (React, Vue, ...) or backend technology (PHP, .NET, Java, ...)?

## UX, Design & frontend application

Aim for questions clarifying requirements on user experience exercises (prototype/wireframes) and visual design. Clarify the baseline where we will start off with for this project (e.g. UX & design can be part of the scope, but it can also be available already and we should only perform the actual build implementation)

### Example questions

- Is UX and design part of the scope of the project? Is there an up-to-date brandbook available?

## AI

Aim for questions clarifying existing AI-maturity at the prospect.

### Example questions

- Has the team started experimenting with AI tooling, either in day-to-day workflows or as part of the platform itself? 

## E-commerce

Aim for questions clarifying the commerce requirements for the project.

### Example questions

- What does the product catalog look like? Do you need an extensive set of filters to browse the product catalog?

- How many active SKUs are there? Are product descriptions and attributes complete and translated for all launch languages, or is data enrichment needed before go-live? 

- Which payment methods are available?

## Team & Governance

Aim for questions clarifying how we will be working together in this project. We want to get a view on the size of the team at the prospect's side and if the people we are working with are decision-makers.

### Example questions

- Who will be involved from the prospect's side? Please confirm the roles: product owner, IT/infrastructure contact, PIM owner, CRM owner, marketing lead, legal/compliance contact etc.

- What is your preferred sprint cadence and review frequency? Who has final sign-off on design, content, and go-live decisions?