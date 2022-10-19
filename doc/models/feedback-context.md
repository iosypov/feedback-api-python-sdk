
# Feedback Context

Feedback object.

## Structure

`FeedbackContext`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `string` | Optional | Page of the feedback. |
| `category` | `string` | Optional | Category of the feedback. |
| `api_operation_id` | `string` | Optional | operationId of the API. |
| `tags` | `List of string` | Optional | Any list of tags to group feedbacks by. |
| `user_id` | `string` | Optional | Unique identifier of the user. |

## Example (as JSON)

```json
{
  "page": null,
  "category": null,
  "apiOperationId": null,
  "tags": null,
  "userId": null
}
```

