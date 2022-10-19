
# Feedback Data

Feedback object.

## Structure

`FeedbackData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rating` | `float` | Optional | Rating of the feedback.<br>**Constraints**: `>= 0` |
| `sentiment` | `bool` | Optional | Sentiment of the feedback. |
| `reasons` | `List of string` | Optional | Reasons of the feedback.<br>**Constraints**: *Minimum Items*: `1` |
| `suggestion` | `string` | Optional | Suggestion of the feedback. |

## Example (as JSON)

```json
{
  "rating": null,
  "sentiment": null,
  "reasons": null,
  "suggestion": null
}
```

