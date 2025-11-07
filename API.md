#  API Documentation — Access Control Service

This document describes all the available REST APIs exposed by the **Access Control Service**.
These APIs allow other services (like the main app) to query user roles, permissions, and perform access validation at both **Office** and **DSO** levels.

---

##  Health Check

**GET /health**

Use this to confirm that the service is running.

**Response:**

```json
{
  "status": "ok",
  "message": "Access Control Service running"
}
```

---

##  Get All Roles for a User

**GET /api/users/<user_id>/roles**

Fetches all the roles assigned to a specific user, whether at the DSO or office level.

**Path Parameter:**
`user_id` – The user’s unique identifier.

**Example Request:**
`GET /api/users/1/roles`

**Response:**

```json
{
  "user_id": 1,
  "roles": [
    { "role": "Office Manager", "scope": "office", "office_id": 101 },
    { "role": "DSO Admin", "scope": "dso", "dso_id": 1 }
  ]
}
```

---

##  Get Offices Under a DSO

**GET /api/dso/<dso_id>/offices**

Fetches all offices managed by a specific DSO.

**Path Parameter:**
`dso_id` – The DSO’s unique identifier.

**Example Request:**
`GET /api/dso/1/offices`

**Response:**

```json
{
  "dso_id": 1,
  "offices": [
    { "office_id": 101, "name": "BrightSmiles LA" },
    { "office_id": 102, "name": "BrightSmiles SF" }
  ]
}
```

---

##  Get DSO for an Office

**GET /api/offices/<office_id>/dso**

Finds which DSO an office belongs to.

**Path Parameter:**
`office_id` – The office’s unique identifier.

**Example Request:**
`GET /api/offices/101/dso`

**Response:**

```json
{
  "office_id": 101,
  "dso": {
    "dso_id": 1,
    "name": "BrightSmiles Dental Group"
  }
}
```

---

##  Check Office-Level Permission

**POST /api/check-permission/office**

Validates if a user has permission to perform an action within a specific office.
Used for office-level users (like Office Managers or Billing Agents).

**Request Body:**

```json
{
  "userId": 2,
  "officeId": 101,
  "action": "edit_records"
}
```

**Response (allowed):**

```json
{
  "allowed": true,
  "scope": "office",
  "granted_by_role": "Office Manager"
}
```

**Response (denied):**

```json
{
  "allowed": false,
  "reason": "User 2 is not authorized to perform 'edit_records' on office 101."
}
```

---

##  Check DSO-Level Permission

**POST /api/check-permission/dso**

Checks if a DSO-level user can perform an action across one of their offices.
Used for roles such as DSO Admin or Regional Manager.

**Request Body:**

```json
{
  "userId": 1,
  "officeId": 102,
  "action": "view_billing"
}
```

**Response (allowed):**

```json
{
  "allowed": true,
  "scope": "dso",
  "granted_by_role": "DSO Admin (DSO Level)"
}
```

**Response (denied):**

```json
{
  "allowed": false,
  "reason": "User 1 is not authorized to perform 'view_billing' on office 102."
}
```

---

##  List All Permissions

**GET /api/permissions**

Lists all available permissions in the system.
Useful for debugging, admin dashboards, or role creation.

**Response:**

```json
{
  "permissions": [
    "view_patients",
    "edit_records",
    "view_billing",
    "edit_billing"
  ]
}
```

---

##  Integration Notes

* Responses always include `allowed: true/false` for easy integration
* User IDs, Office IDs, and DSO IDs should match existing records in the main database or seed data
* This service is **read-heavy** and can be easily cached at the API Gateway level

---

##  Example Workflow

1. Main app sends user ID, office ID, and action to `/check-permission`
2. Microservice validates:

   * User’s role and scope
   * Office-to-DSO relationship
   * Role permissions from the database
3. Returns a simple decision:

   ```json
   { "allowed": true ,"reason": "Granted by role at office 1"}
   ```

   or

   ```json
   { "allowed": false, "reason": "Insufficient permissions" }
   ```

---

## 📘 Notes

* DSO-level and Office-level users are maintained separately.
* DSO users can have access to multiple offices under their DSO.
* Office users are tied to one specific office.
* The permission model can be extended easily with new actions and roles.