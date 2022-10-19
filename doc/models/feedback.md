
# Feedback

## Structure

`Feedback`

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
| `id` | `string` | Required | Unique identifier of the feedback. |
| `created_at` | `datetime` | Required | Date of the feedback creation. |
| `updated_at` | `datetime` | Optional | Date of the feedback update. |
| `user_ip` | `string` | Required | IP address of the user. |
| `user_agent` | `string` | Required | User agent of the device. |

## Example (as JSON)

```json
{
  "id": "c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd",
  "createdAt": "01/01/2020 00:00:00",
  "userIP": "91.201.190.10",
  "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
```

