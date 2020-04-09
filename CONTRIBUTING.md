# Contributing to GLO-2005 (H2020) - Team 8 project

**Contributions are welcome!**

## Code of conduct

Before contributing to the project, please read our [code of conduct](CODE_OF_CONDUCT.md).

## Task tracking

### Issues

We track our issues with GitHub issues. Each issue must have at least one person assigned, a date of delivery, an associated milestone and correct labels.

Milestones represent release numbers. For example, release 1 would be milestone `1`. `1.1` would be release 1 hotfix.

### Project board

Issues must be placed on the [project board](https://github.com/ExiledNarwal28/glo-2005-project/projects/2). There are 5 columns in this board : 

- Maybe : Optional issues that are not prioritized in the current sprint
- Backlog : Issues that must be done to deliver the current iteration
- In progress : Self-explanatory
- In review : Issues currently in review
- Done : Closed issues (see : Definition of done)

The person in charge of an issue is in charge of moving it across the project board.

### Bug reporting

When a bug is spotted in the application, it must be reported as an issue on GitHub issues. There is a `bug` label. It must be added in the ToDo column of the project, above all non-bugs issues, ordered by priority.

### Pull requests

We use trunk based development with `master` as a main branch. Every PR adding a feature to the application or solving a bug must be merged into `master`.

For each issue, there must be at least one PR (more PRs could be added if the issue is reopened). This PR must build. Also, two reviewers must approve the PR before it is merged into `master`.

To follow this trend, PR names are as following : `What is added` (ex : `Add shops views`).

The one in charge of merging the PR is the one in charge of the associated issue.

To review a PR is a lot of things. First, you must read each added line, understand them, make sur they make sense and point out if there is any way to improve it. You must then pull the branch, test the app, make sure it works in execution using Postman and call it a day. Only approve PRs that are 100% ready to merge. Otherwise, request changes explaining clearly what must be added for approval.

### When is a milestone achieved / Definition of done

A milestone is achieved once every of its issues are solved. This includes everything to add for a new release, from adding features, to solving bugs and improving performance.

Issues are closed once all described tasks are confirmed done by the reviewers, which only means that the PR is closed. This requires reviewing code style, quality, tests and actual functionality of said PR.

## Development

### Code style

No comment should be in the source code. Some exceptions are small explanations. In those rare cases, comments are clear and tiny.

TODOs are okay, as long as they do not make it to the release. They can be used to mark where a certain issue must be done (in which case, an issue number is much appreciated). In almost all other cases, they should be removed an converted to an actual issue.

### Test driven development

Every single piece of code added to the application must be written using test driven development. For TDD, we follow the tree basic steps : write failing tests for new feature, write basic code to get tests to pass and finally reformat newly added code. Once the new feature is correctly implemented, commit.

Tests are located in `app/tests`. Test file names must have a `test_` prefix. For instance, the test file name for `shop/views.py` would be `shop/test_views.py`. Test class names must have a `Tests` suffix. For instance, the test class for `ShopViews` would be `ShopViewTests`.

Set up of tests must be extracted as much as possible from unit tests.

### Git

Normally, every branch is a fork of `master`. Some exceptions are features building upon PRs that are not done being reviewed.

Our branch names are as following : `whatIsAdded` (ex : `addShopRepositories`). Always camelcase.

We try, as much as possible, to format commit messages as following : `What is added` (ex : `Add mocks of shops in basic view tests`).

When a PR is merged, the associated branch is deleted as we do not want unnecessary unmaintained branches on our remote.

## Contributors

- Fabien Roy / ExiledNarwal28
- Mikaël Valliant / mikaelvalliant
