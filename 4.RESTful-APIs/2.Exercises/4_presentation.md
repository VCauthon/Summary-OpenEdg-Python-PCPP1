## Estimated time
20-30 minutes

## Level of difficulty
Medium

## Objectives
Learn how to:
- Use the requests module facilities;
- Interpret server responses.

## Scenario

Now we want to you to return to the issues discussed in lab #1. In fact, you need to implement exactly the same functionality as you embedded in your code previously, but this time you have to use the requests module instead of the socket module. Everything else should remain the same: the command line arguments and outputs have to be indistinguishable.

__Hint__: use the `head()` method instead of `get()`, as you don't need the whole root document the server sends to you — the header is enough to test whether or not the server is responding. Fortunately, `head()` has exactly the same interface as `get()`. Don't forget to handle all needed exceptions — don't leave your user without any clear explanations about anything that went wrong.