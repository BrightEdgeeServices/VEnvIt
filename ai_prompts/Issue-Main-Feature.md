Create the text for a Linear (www.https://linear.app/) issue for this project.

# Problem description in my words:

[Insert the description in your own words in here]

# Solution in my words:

[Insert the objective in your own words in here]

# Instructions

1. Create one issue for the entire project.
1. This will serve as the "main feature branch" and will have several sub-issues.
1. Create an issue title/subject.
1. Create git branch name in the following format: “`mf`-`repo`-`Insert Title Here`" where `mf` is “fixed text”, `repo` is the “name” of the repo and `Insert Title Here` is a short description to complete the branch name
1. The git branch name must be less than 50 characters.
1. "Success Criteria" in the template below define high-level measurable outcomes that determine whether this initiative is complete.
1. "Deployment Checks" in the template below must be a high-level checklist to all the steps are followed to deploy the code.
1. Keep it as high-level as possible.
1. Add more items to "Success Criteria" and "Deployment Checks" if you think it is necessary
1. Do not resort to using sub-bullets under subheadings in "Success Criteria" and "Deployment Checks". All tasks must be at the top level.
1. Do not duplicate items between "Success Criteria" and "Deployment Checks".
1. Propose the titles for the sub issues to complete this piece of work
1. Write the output to a Markdown file in the "legacy" directory on the project root. If it does not exist, create it.
1. The name of the file is the name of the issue.

# Use the following template headings to generate the text for the Linear issue:

1. "Description of Feature or Improvement"
1. "Proposed Solution"
1. "Success Criteria"
   - [ ] New tests are implemented for new functionality
   - [ ] Old tests are adapted to for code changes.
   - [ ] All tests are successful.
   - [ ] ReleaseNotes are updated
1. "Deployment Checks"
   - [ ] Commented GitHub Workflows scripts for testing purposes are restored.
   - [ ] CI is successful for all feature branches.
   - [ ] Merged into master.
   - [ ] ReleaseNotes are published.
   - [ ] Deleted related development branches.
   - [ ] Complete the project in Linear if done.
