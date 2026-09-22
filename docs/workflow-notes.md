# Workflow Notes

## Change Flow: Idea → Released

1. **Idea** — A new requirement or bug is identified.
2. **Issue** — The idea is logged as a GitHub Issue (using the Bug Report or 
   Feature Request template), describing the problem or feature clearly.
   *QA involvement: QA reviews the issue for clarity, reproducibility (for 
   bugs), and testability before it's picked up.*
3. **Branch** — A developer creates a feature/fix branch off `main`, 
   following the naming convention (`feature/<slug>`, `fix/<slug>`).
4. **Development & Commits** — Code is written and committed in small, 
   atomic commits using Conventional Commits format.
5. **Pull Request (PR)** — The branch is pushed and a PR is opened against 
   `main`, referencing the original issue.
   *QA involvement: This is the primary quality gate. QA (or a peer) 
   reviews the diff for correctness, missing tests, and edge cases.*
6. **Review** — At least one approval is required (enforced by branch 
   protection) before the PR can be merged.
7. **Merge** — The PR is merged into `main` using Squash and Merge to 
   keep history linear.
8. **CI** — Automated checks run against the merged code (to be configured 
   in a later lab).
   *QA involvement: QA defines and maintains the automated test suite 
   that CI runs, catching regressions before release.*
9. **Release** — Once CI passes and the code is verified, it is released.
   *QA involvement: QA performs final verification/acceptance checks 
   before sign-off.*

## Summary
QA is not a single step at the end — it's embedded at the Issue stage 
(clarity/testability), the PR/Review stage (catching defects early), 
the CI stage (automated regression prevention), and the Release stage 
(final verification).
