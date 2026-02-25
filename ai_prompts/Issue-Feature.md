Create the text for a Linear (www.https://linear.app/) sub-issue for the main-feature branch.

# Problem description in my words:

[Insert the description of the work subset in your own words in here]
Example: "Write a description that extracts the information from the main-feature branch related to bla,bla,bla…"

# Solution in my words:

[Insert the objective of the work subset in your own words in here]
Example: "Write the solution to satisfy the problem description as above."

# Instructions

1. Create only one issue for the description above.
1. This will serve as a "feature branch" and sub feature of the "main feature branch".
1. Create git branch name in the following format: “`feat`-`repo`-`Insert Title Here`" where `feat` is “fixed text”, `repo` is the “name” of the repo and `Insert Title Here` is a short description to complete the branch name
1. The git branch name must be less than 55 characters.
1. Keep it as high-level as possible.
1. "Success Criteria" in the template below define high-level measurable outcomes that determine whether this work subset completes.
1. Add more items to "Success Criteria" and "Completion Checks" if you think it is necessary
1. Do not use sub-bullets under subheadings in "Success Criteria" and "Completion Checks". All tasks must be at the top level.
1. Do not duplicate items between "Success Criteria" and "Completion Checks".
1. Write the output to a Markdown file in the "legacy" directory on the project root. If it does not exist, create it.
1. The file name is the branch name.

# Use the template and additional instructions below to create a Linear issue:

1. “Description” of the work subset.
1. “Proposed Solution” for the work subset.
1. “Success Criteria”
   Define the measurable outcomes that determine whether this initiative is complete:
   - [ ] New tests are implemented for new functionality
   - [ ] Old tests are adapted to for code changes.
   - [ ] All tests are successful.
1. “Completion Checks”: Add more if you think it is necessary
   - [ ] Commented GitHub Workflows scripts for testing purposes are restored.
   - [ ] Functions/methods/variables in modules are in alphabetical order (if possible).
   - [ ] CI is successful.
   - [ ] CodeCov above 99% or justifiably less.
   - [ ] Commented code not useful any more is removed.
   - [ ] Remove warnings, errors and spelling reported by IDE.
   - [ ] Update / remove Todo’s
   - [ ] Deleted related development branches.
   - [ ] CodeCov above 99% or justifiably less.
   - [ ] Merged into main_feature.
