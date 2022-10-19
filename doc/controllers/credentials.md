# Credentials

```python
credentials_controller = client.credentials
```

## Class Name

`CredentialsController`

## Methods

* [Create Credentials](../../doc/controllers/credentials.md#create-credentials)
* [Rotate Credentials](../../doc/controllers/credentials.md#rotate-credentials)
* [Delete Credentials](../../doc/controllers/credentials.md#delete-credentials)


# Create Credentials

### Start here by creating your credentials

Be careful to save the private key that is returned. You will not be able to retrieve it again.
You can only have one private key at a time.
Private key is not to be shared with anyone, do not expose it in your frontend code.

```python
def create_credentials(self)
```

## Response Type

[`Credentials`](../../doc/models/credentials.md)

## Example Usage

```python
result = credentials_controller.create_credentials()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Rotate Credentials

### Rotate credentials

Generate a new private key and invalidate the current one.
Use this in case your private key is compromised or for security reasons.

```python
def rotate_credentials(self,
                      x_api_key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_api_key` | `string` | Header, Required | Private key. Create a tenant to generate. |

## Response Type

[`Credentials`](../../doc/models/credentials.md)

## Example Usage

```python
x_api_key = 'X-API-KEY2'

result = credentials_controller.rotate_credentials(x_api_key)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |


# Delete Credentials

### Delete credentials

Invalidate your current private key.
You will no longer be able to create or read feedback.

```python
def delete_credentials(self,
                      x_api_key)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_api_key` | `string` | Header, Required | Private key. Create a tenant to generate. |

## Response Type

`void`

## Example Usage

```python
x_api_key = 'X-API-KEY2'

result = credentials_controller.delete_credentials(x_api_key)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`UnauthorizedException`](../../doc/models/unauthorized-exception.md) |
| 429 | Too Many Requests | [`TooManyRequestsException`](../../doc/models/too-many-requests-exception.md) |
| 500 | Internal Server Error | [`InternalServerErrorException`](../../doc/models/internal-server-error-exception.md) |

