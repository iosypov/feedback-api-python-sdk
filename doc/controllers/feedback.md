# Feedback

```python
feedback_controller = client.feedback
```

## Class Name

`FeedbackController`

## Methods

* [Create Feedback](../../doc/controllers/feedback.md#create-feedback)
* [Get Feedback](../../doc/controllers/feedback.md#get-feedback)
* [Get Feedback by Id](../../doc/controllers/feedback.md#get-feedback-by-id)
* [Update Feedback by Id](../../doc/controllers/feedback.md#update-feedback-by-id)


# Create Feedback

### Create a new feedback

You can explore sample payloads below.
Every feedback must have at least one properties:

- `rating`: numeric value (star rating)
- `sentiment`: boolean value (like/dislike button)
- `reasons`: list of text values (multiple choice questions)
- `suggestion`: text value (free text input)

In addition, you may provide any of context values:

- `userId`: string value (for logged in users, we'll generate one for anonymous users)
- `page`: text value (url of the page where the feedback was given)
- `category`: text value (category of the page where the feedback was given)
- `apiOperationId`: text value (operationId for OpenAPI docs)
- `tags`: list of text values (product name, feature name, etc.)

```python
def create_feedback(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FeedbackReq`](../../doc/models/feedback-req.md) | Body, Required | - |

## Response Type

[`Feedback`](../../doc/models/feedback.md)

## Example Usage

```python
body = FeedbackReq()
body.rating = 4
body.suggestion = 'Some screenshots would help'
body.page = 'https://example.com/docs/tutorial/1'
body.user_id = 'abc-xyz'

result = feedback_controller.create_feedback(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Feedback

Get feedback.

```python
def get_feedback(self,
                x_api_key,
                rating=None,
                sentiment=None,
                reasons=None,
                user_id=None,
                user_ip=None,
                page=None,
                category=None,
                api_operation_id=None,
                tags=None,
                x_page=1,
                x_per_page=50,
                x_order='desc',
                x_order_by='createdAt')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_api_key` | `string` | Header, Required | Private key. Create a tenant to generate. |
| `rating` | `List of float` | Query, Optional | Rating to filter by.<br>**Constraints**: `>= 0` |
| `sentiment` | `List of bool` | Query, Optional | Sentiment to filter by. |
| `reasons` | `List of string` | Query, Optional | Reasons to filter by. |
| `user_id` | `List of string` | Query, Optional | User ID to filter by. |
| `user_ip` | `List of string` | Query, Optional | IP address to filter by. |
| `page` | `List of string` | Query, Optional | Page to filter by. |
| `category` | `List of string` | Query, Optional | Category to filter by. |
| `api_operation_id` | `List of string` | Query, Optional | Operation to filter by. |
| `tags` | `List of string` | Query, Optional | Tags to filter by. |
| `x_page` | `float` | Header, Optional | Page number.<br>**Default**: `1` |
| `x_per_page` | `float` | Header, Optional | Items per page.<br>**Default**: `50` |
| `x_order` | [`XORDEREnum`](../../doc/models/xorder-enum.md) | Header, Optional | Sort order.<br>**Default**: `'desc'` |
| `x_order_by` | [`XORDERBYEnum`](../../doc/models/xorderby-enum.md) | Header, Optional | Order by.<br>**Default**: `'createdAt'` |

## Response Type

[`FeedbackResponse`](../../doc/models/feedback-response.md)

## Example Usage

```python
x_api_key = 'X-API-KEY2'
x_page = 1
x_per_page = 10
x_order = XORDEREnum.DESC
x_order_by = XORDERBYEnum.CREATEDAT

result = feedback_controller.get_feedback(x_api_key, None, None, None, None, None, None, None, None, None, x_page, x_per_page, x_order, x_order_by)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Get Feedback by Id

Get feedback by id.

```python
def get_feedback_by_id(self,
                      id,
                      x_api_key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Resource identifier string.<br>**Constraints**: *Pattern*: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$` |
| `x_api_key` | `string` | Header, Required | Private key. Create a tenant to generate. |

## Response Type

[`Feedback`](../../doc/models/feedback.md)

## Example Usage

```python
id = 'c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd'
x_api_key = 'X-API-KEY2'

result = feedback_controller.get_feedback_by_id(id, x_api_key)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 404 | Not found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Update Feedback by Id

Update feedback by id.

```python
def update_feedback_by_id(self,
                         id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | Resource identifier string.<br>**Constraints**: *Pattern*: `^[0-9a-fA-F]{8}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{4}\b-[0-9a-fA-F]{12}$` |
| `body` | [`FeedbackReq`](../../doc/models/feedback-req.md) | Body, Required | - |

## Response Type

[`Feedback`](../../doc/models/feedback.md)

## Example Usage

```python
id = 'c73bcdcc-2669-4bf6-81d3-e4ae73fb11fd'
body = FeedbackReq()
body.rating = 4
body.user_id = 'abc-xyz'

result = feedback_controller.update_feedback_by_id(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`BadRequestException`](../../doc/models/bad-request-exception.md) |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 404 | Not found | [`NotFoundException`](../../doc/models/not-found-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

