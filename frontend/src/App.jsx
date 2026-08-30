import { useEffect, useState } from 'react';
import { employeeApi, emptyEmployeeForm } from './api/employees';
import './App.css';

function App() {
  const [employees, setEmployees] = useState([]);
  const [form, setForm] = useState(emptyEmployeeForm());
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState('');
  const [notice, setNotice] = useState('');
  const [query, setQuery] = useState('');

  async function loadEmployees() {
    setLoading(true);
    setError('');
    try {
      const rows = await employeeApi.list();
      setEmployees(rows);
    } catch (err) {
      setError(err.message || 'Failed to load employees');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadEmployees();
  }, []);

  function updateField(field, value) {
    setForm((prev) => ({ ...prev, [field]: value }));
  }

  function updateAddress(field, value) {
    setForm((prev) => ({
      ...prev,
      employee_address: { ...prev.employee_address, [field]: value },
    }));
  }

  function resetForm() {
    setForm(emptyEmployeeForm());
    setEditingId(null);
  }

  function startEdit(emp) {
    setEditingId(emp.employee_id);
    setForm({
      employee_name: emp.employee_name,
      employee_age: String(emp.employee_age),
      employee_salary: String(emp.employee_salary),
      employee_email: emp.employee_email,
      employee_address: {
        employee_doorno: String(emp.employee_address.employee_doorno),
        employee_streetname: emp.employee_address.employee_streetname,
        employee_city: emp.employee_address.employee_city,
        employee_pincode: String(emp.employee_address.employee_pincode),
      },
    });
    setNotice('');
    setError('');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setSaving(true);
    setError('');
    setNotice('');
    try {
      if (editingId == null) {
        const res = await employeeApi.create(form);
        setNotice(res?.message || 'Employee added');
      } else {
        const res = await employeeApi.update(editingId, form);
        setNotice(res?.message || 'Employee updated');
      }
      resetForm();
      await loadEmployees();
    } catch (err) {
      setError(err.message || 'Save failed');
    } finally {
      setSaving(false);
    }
  }

  async function handleDelete(id) {
    if (!window.confirm(`Delete employee #${id}?`)) return;
    setError('');
    setNotice('');
    try {
      const res = await employeeApi.remove(id);
      setNotice(res?.message || 'Deleted');
      if (editingId === id) resetForm();
      await loadEmployees();
    } catch (err) {
      setError(err.message || 'Delete failed');
    }
  }

  const filtered = employees.filter((emp) => {
    const q = query.trim().toLowerCase();
    if (!q) return true;
    return (
      String(emp.employee_id).includes(q) ||
      emp.employee_name.toLowerCase().includes(q) ||
      emp.employee_email.toLowerCase().includes(q) ||
      emp.employee_address.employee_city.toLowerCase().includes(q)
    );
  });

  return (
    <div className="app">
      <div className="bg-grid" aria-hidden="true" />

      <header className="top">
        <div className="brand-block">
          <p className="brand">EMS</p>
          <h1>Employee desk</h1>
          <p className="lede">
            Manage people records against the FastAPI SQLite backend.
          </p>
        </div>
        <div className="top-meta">
          <span className="pill">{employees.length} on file</span>
          <button type="button" className="ghost" onClick={loadEmployees}>
            Refresh
          </button>
        </div>
      </header>

      <main className="layout">
        <section className="panel form-panel">
          <div className="panel-head">
            <h2>{editingId == null ? 'Add employee' : `Edit #${editingId}`}</h2>
            {editingId != null && (
              <button type="button" className="ghost" onClick={resetForm}>
                Cancel edit
              </button>
            )}
          </div>

          <form className="form" onSubmit={handleSubmit}>
            <label>
              Name
              <input
                required
                value={form.employee_name}
                onChange={(e) => updateField('employee_name', e.target.value)}
              />
            </label>
            <div className="row">
              <label>
                Age
                <input
                  required
                  type="number"
                  min="0"
                  value={form.employee_age}
                  onChange={(e) => updateField('employee_age', e.target.value)}
                />
              </label>
              <label>
                Salary
                <input
                  required
                  type="number"
                  min="0"
                  value={form.employee_salary}
                  onChange={(e) => updateField('employee_salary', e.target.value)}
                />
              </label>
            </div>
            <label>
              Email
              <input
                required
                type="email"
                value={form.employee_email}
                onChange={(e) => updateField('employee_email', e.target.value)}
              />
            </label>

            <p className="section-label">Address</p>
            <div className="row">
              <label>
                Door no.
                <input
                  required
                  type="number"
                  min="0"
                  value={form.employee_address.employee_doorno}
                  onChange={(e) => updateAddress('employee_doorno', e.target.value)}
                />
              </label>
              <label>
                Pincode
                <input
                  required
                  type="number"
                  min="0"
                  value={form.employee_address.employee_pincode}
                  onChange={(e) => updateAddress('employee_pincode', e.target.value)}
                />
              </label>
            </div>
            <label>
              Street
              <input
                required
                value={form.employee_address.employee_streetname}
                onChange={(e) => updateAddress('employee_streetname', e.target.value)}
              />
            </label>
            <label>
              City
              <input
                required
                value={form.employee_address.employee_city}
                onChange={(e) => updateAddress('employee_city', e.target.value)}
              />
            </label>

            <button type="submit" className="primary" disabled={saving}>
              {saving ? 'Saving…' : editingId == null ? 'Create employee' : 'Save changes'}
            </button>
          </form>

          {error && <p className="banner error">{error}</p>}
          {notice && <p className="banner ok">{notice}</p>}
        </section>

        <section className="panel list-panel">
          <div className="panel-head">
            <h2>Directory</h2>
            <input
              className="search"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search name, email, city, id"
            />
          </div>

          {loading ? (
            <p className="muted">Loading employees…</p>
          ) : filtered.length === 0 ? (
            <p className="muted">No employees match.</p>
          ) : (
            <div className="table-wrap">
              <table>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Age</th>
                    <th>Salary</th>
                    <th>City</th>
                    <th />
                  </tr>
                </thead>
                <tbody>
                  {filtered.map((emp) => (
                    <tr key={emp.employee_id}>
                      <td>{emp.employee_id}</td>
                      <td>{emp.employee_name}</td>
                      <td>{emp.employee_email}</td>
                      <td>{emp.employee_age}</td>
                      <td>{emp.employee_salary}</td>
                      <td>{emp.employee_address.employee_city}</td>
                      <td className="actions">
                        <button type="button" className="ghost" onClick={() => startEdit(emp)}>
                          Edit
                        </button>
                        <button
                          type="button"
                          className="danger"
                          onClick={() => handleDelete(emp.employee_id)}
                        >
                          Delete
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}

export default App;
