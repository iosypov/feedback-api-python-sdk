
# Feedback Req

## Structure

`FeedbackReq`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rating` | `float` | Optional | Rating of the feedback.<br>**Constraints**: `>= 0` |
| `sentiment` | `bool` | Optional | Sentiment of the feedback. |
| `reasons` | `List of string` | Optional | Reasons of the feedback.<br>**Constraints**: *Minimum Items*: `1` |
| `suggestion` | `string` | Optional | Suggestion of the feedback. |
| `page` | `string` | Optional | Page of the feedback. |
| `category` | `string` | Optional | Category of the feedback. |
| `api_operation_id` | `string` | Optional | operationId of the API. |
| `tags` | `List of string` | Optional | Any list of tags to group feedbacks by. |
| `user_id` | `string` | Optional | Unique identifier of the user. |

## Example (as JSON)

```json
{
  "rating": null,
  "sentiment": null,
  "reasons": null,
  "suggestion": null,
  "page": null,
  "category": null,
  "apiOperationId": null,
  "tags": null,
  "userId": null
}
```

