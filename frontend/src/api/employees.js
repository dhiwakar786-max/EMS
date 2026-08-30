const API_BASE = import.meta.env.VITE_API_BASE ?? '';

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  });

  let data = null;
  const text = await response.text();
  if (text) {
    try {
      data = JSON.parse(text);
    } catch {
      data = text;
    }
  }

  if (!response.ok) {
    const detail =
      typeof data === 'object' && data?.detail
        ? typeof data.detail === 'string'
          ? data.detail
          : JSON.stringify(data.detail)
        : response.statusText;
    throw new Error(detail || 'Request failed');
  }

  return data;
}

/** Backend list/get use employee_dooorno; create/update expect employee_doorno. */
export function normalizeEmployee(emp) {
  if (!emp) return null;
  const addr = emp.employee_address || {};
  return {
    employee_id: emp.employee_id,
    employee_name: emp.employee_name,
    employee_age: emp.employee_age,
    employee_salary: emp.employee_salary,
    employee_email: emp.employee_email,
    employee_address: {
      // map backend typo employee_dooorno → employee_doorno (no invented values)
      employee_doorno: addr.employee_doorno ?? addr.employee_dooorno,
      employee_streetname: addr.employee_streetname,
      employee_city: addr.employee_city,
      employee_pincode: addr.employee_pincode,
    },
  };
}

export function emptyEmployeeForm() {
  return {
    employee_name: '',
    employee_age: '',
    employee_salary: '',
    employee_email: '',
    employee_address: {
      employee_doorno: '',
      employee_streetname: '',
      employee_city: '',
      employee_pincode: '',
    },
  };
}

function toCreatePayload(form) {
  return {
    employee_name: form.employee_name.trim(),
    employee_age: Number(form.employee_age),
    employee_salary: Number(form.employee_salary),
    employee_email: form.employee_email.trim(),
    employee_address: {
      employee_doorno: Number(form.employee_address.employee_doorno),
      employee_streetname: form.employee_address.employee_streetname.trim(),
      employee_city: form.employee_address.employee_city.trim(),
      employee_pincode: Number(form.employee_address.employee_pincode),
    },
  };
}

function toUpdatePayload(form) {
  return {
    employee_name: form.employee_name.trim(),
    employee_age: Number(form.employee_age),
    employee_salary: Number(form.employee_salary),
    employee_email: form.employee_email.trim(),
    employee_address: {
      employee_doorno: Number(form.employee_address.employee_doorno),
      employee_streetname: form.employee_address.employee_streetname.trim(),
      employee_city: form.employee_address.employee_city.trim(),
      employee_pincode: Number(form.employee_address.employee_pincode),
    },
  };
}

export const employeeApi = {
  async list() {
    const data = await request('/api/v1/employees/');
    const rows = Array.isArray(data?.result) ? data.result : [];
    return rows.map(normalizeEmployee);
  },

  async get(id) {
    const data = await request(`/api/v1/employees/${id}`);
    return normalizeEmployee(data?.message);
  },

  async create(form) {
    return request('/api/v1/employees/', {
      method: 'POST',
      body: JSON.stringify(toCreatePayload(form)),
    });
  },

  async update(id, form) {
    return request(`/api/v1/employees/${id}`, {
      method: 'PUT',
      body: JSON.stringify(toUpdatePayload(form)),
    });
  },

  async updateName(id, employee_name) {
    return request(`/api/v1/employees/${id}/name`, {
      method: 'PUT',
      body: JSON.stringify({ employee_name }),
    });
  },

  async updateEmail(id, employee_email) {
    return request(`/api/v1/employees/${id}/email`, {
      method: 'PUT',
      body: JSON.stringify({ employee_email }),
    });
  },

  async remove(id) {
    return request(`/api/v1/employees/${id}`, {
      method: 'DELETE',
    });
  },
};
