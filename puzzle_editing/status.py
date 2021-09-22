# Just a fake enum and namespace to keep status-related things in. If we use a
# real Enum, Django weirdly doesn't want to display the human-readable version.

INITIAL_IDEA = "II"  # aka. Concept stage
WRITING = "W"
TESTSOLVING = "T"
REVISING = "R"
NEEDS_SOLUTION = "NS"  # aka.
DONE = "D"
DEAD = "X"

# for ordering
# unclear if this was a good idea, but it does mean we can insert and reorder
# statuses without a database migration (?)
STATUSES = [
    INITIAL_IDEA,
    WRITING,
    TESTSOLVING,
    REVISING,
    NEEDS_SOLUTION,
    DONE,
    DEAD,
]


def get_status_rank(status):
    try:
        return STATUSES.index(status)
    except ValueError:  # not worth crashing imo
        return -1


def past_writing(status):
    return get_status_rank(status) > get_status_rank(WRITING) and get_status_rank(
        status
    ) <= get_status_rank(DONE)


def past_testsolving(status):
    return get_status_rank(status) > get_status_rank(REVISING) and get_status_rank(
        status
    ) <= get_status_rank(DONE)


# a partition of the statuses that excludes Done or Dead for some queries
PRE_TESTSOLVING_STATUSES = STATUSES[: STATUSES.index(TESTSOLVING)]
POST_TESTSOLVING_STATUSES = STATUSES[STATUSES.index(TESTSOLVING) : STATUSES.index(DONE)]

# Possible blockers:

EDITORS = "editors"
AUTHORS = "authors"
TESTSOLVERS = "testsolvers"
POSTPRODDERS = "postprodders"
FACTCHECKERS = "factcheckers"
NOBODY = "nobody"

BLOCKERS_AND_TRANSITIONS = {
    INITIAL_IDEA: (
        AUTHORS,
        [(DEAD, "⏹️  Mark as dead"), (WRITING, "✅ Start writing puzzle")],
    ),
    WRITING: (AUTHORS, [(TESTSOLVING, "✅ Put into testsolving")]),
    TESTSOLVING: (
        TESTSOLVERS,
        [
            (REVISING, "❌ Request puzzle revision"),
            (NEEDS_SOLUTION, "✅ Accept testsolve; request solution from authors"),
        ],
    ),
    REVISING: (
        AUTHORS,
        [
            (TESTSOLVING, "⏩ Put into testsolving"),
            (NEEDS_SOLUTION, "⏩ Done revising; requesting solution & hints"),
        ],
    ),
    NEEDS_SOLUTION: (
        AUTHORS,
        [
            (DONE, "⏩🎆 Mark as done! 🎆⏩"),
        ],
    ),
}


def get_blocker(status):
    value = BLOCKERS_AND_TRANSITIONS.get(status)
    if value:
        return value[0]
    else:
        return NOBODY


def get_transitions(status):
    value = BLOCKERS_AND_TRANSITIONS.get(status)
    if value:
        return value[1]
    else:
        return []


STATUSES_BLOCKED_ON_EDITORS = [
    status
    for status, (blocker, _) in BLOCKERS_AND_TRANSITIONS.items()
    if blocker == EDITORS
]
STATUSES_BLOCKED_ON_AUTHORS = [
    status
    for status, (blocker, _) in BLOCKERS_AND_TRANSITIONS.items()
    if blocker == AUTHORS
]

DESCRIPTIONS = {
    INITIAL_IDEA: "Concept",
    WRITING: "Writing",
    TESTSOLVING: "Testsolving",
    REVISING: "Revising",
    NEEDS_SOLUTION: "Needs Solution & Hints",
    DONE: "Done",
    DEAD: "Dead",
}

MAX_LENGTH = 2


def get_display(status):
    return DESCRIPTIONS.get(status, status)


ALL_STATUSES = [
    {
        "value": status,
        "display": description,
    }
    for status, description in DESCRIPTIONS.items()
]
