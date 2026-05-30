# Data Quality Without a Platform Team

Data quality is often treated like a luxury—something you only focus on when you have the resources to build a dedicated platform team. But what if you don’t? What if you’re a solo data engineer or part of a small team? Is data quality still achievable, or are you doomed to live with a mountain of errors and inconsistencies? Spoiler: you can absolutely manage data quality without a full-fledged team, and here’s how.

In many organizations, data quality issues arise simply because there's no one to own the process. It’s too easy to let things slide when you’re juggling multiple roles. But the cost of poor data quality is staggering. From bad business decisions to wasted resources, the implications can be dire. So, how can you enforce data quality checks without a platform team? Let’s break it down.

## Embrace Testing Frameworks

First off, if you're not using testing frameworks like **dbt** or **Great Expectations**, you’re missing a trick. These tools are game-changers for ensuring data quality. They allow you to define expectations and run tests on your data models easily.

With **dbt**, you can create tests directly alongside your models. For example, if you're working with a user table, you might want to ensure that email addresses are unique:

```sql
-- dbt test for unique email addresses
select 
    email, 
    count(*) 
from 
    {{ ref('users') }} 
group by 
    email 
having 
    count(*) > 1
```

When you run this test, dbt will notify you if any duplicates exist. This is a simple yet effective way to spot errors before they escalate.

On the other hand, **Great Expectations** offers a more interactive way to create and manage your data quality checks. You can define what "good" data looks like and run checks against your datasets. This is especially useful if your data is coming from various sources and needs to meet specific standards.

## Automate Checks Where Possible

Automation is your best friend. If you’re still doing manual checks, you’re setting yourself up for disaster. Schedule your tests to run automatically—daily, weekly, or whatever cadence works best for your team. Set up alerts to notify you when something fails. This way, you can act quickly rather than waiting for someone to discover an issue weeks later.

Consider using a CI/CD pipeline to run your tests. If you have a setup that allows for automated deployment, integrate your data quality checks into that workflow. This not only catches errors but also ensures that any new changes are validated against your quality standards right off the bat.

## Foster a Data Quality Culture

Even if you don’t have a dedicated platform team, you can still foster a culture of data quality within your organization. Encourage team members to think about data quality as they work. Make it part of the conversation—whether you’re discussing project planning or sprint reviews. 

Documentation is key here. When you find issues or establish best practices, write them down. Create a living document that outlines common pitfalls and how to avoid them. Share this with your team, so everyone is on the same page.

### Bottom line

You don't need a platform team to achieve high data quality. With the right tools, automation, and a culture that prioritizes data integrity, you can manage quality effectively, even as a solo act. Don’t let a lack of resources hold you back. Embrace the tools at your disposal and make data quality a priority. Your future self will thank you.