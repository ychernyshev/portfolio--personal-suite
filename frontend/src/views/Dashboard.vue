<script setup></script>

<template>
  <div class="container-fliud p-4">
    <div class="row">
      <div class="col-xxl-6">
        <div class="card rounded-3 p-4">
          <h4>
            TOTAL GENERATED POWER:
            <span class="badge text-bg-secondary">30195.35WATT</span>
          </h4>
          Graph
        </div>
      </div>
      <div class="col-xxl-6">
        <div class="card rounded-3 p-4">
          <h4>
            COST OF GENERATED POWER:
            <span class="badge text-bg-secondary">131.90UAH</span>
          </h4>
          Graph
        </div>
      </div>
    </div>
    <div class="row mt-4">
      <div class="col-xxl-12">
        <div class="card rounded-3 p-4">
          <div class="row">
            <div class="col-xxl-3">
              <div class="mb-3">
                <label for="formFileSm" class="form-label">Import data</label>
                <input
                  class="form-control form-control-sm"
                  id="formFileSm"
                  type="file"
                />
              </div>
            </div>
            <div class="col-xxl-3">
              <button
                type="button"
                class="btn btn-light"
                style="margin-top: 1.8rem"
              >
                Export data
              </button>
            </div>
          </div>
          <table class="table table-striped">
            <thead>
              <tr>
                <th scope="col" class="text-center">Date</th>
                <th scope="col" class="text-center">Power</th>
                <th scope="col" class="text-center">Weather indicators</th>
                <th scope="col" class="text-center">Morning indicators</th>
                <th scope="col" class="text-center">Afternoon indicators</th>
                <th scope="col" class="text-center">Evening indicators</th>
                <th scope="col" class="text-center">Energy generated</th>
                <th scope="col" class="text-center">Total cost</th>
                <th scope="col" class="text-center">Tariff</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row" class="text-center">21.09.2025</th>
                <td class="text-center">400</td>
                <td class="text-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-snow2"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 16a.5.5 0 0 1-.5-.5v-1.293l-.646.647a.5.5 0 0 1-.707-.708L7.5 12.793v-1.086l-.646.647a.5.5 0 0 1-.707-.708L7.5 10.293V8.866l-1.236.713-.495 1.85a.5.5 0 1 1-.966-.26l.237-.882-.94.542-.496 1.85a.5.5 0 1 1-.966-.26l.237-.882-1.12.646a.5.5 0 0 1-.5-.866l1.12-.646-.884-.237a.5.5 0 1 1 .26-.966l1.848.495.94-.542-.882-.237a.5.5 0 1 1 .258-.966l1.85.495L7 8l-1.236-.713-1.849.495a.5.5 0 1 1-.258-.966l.883-.237-.94-.542-1.85.495a.5.5 0 0 1-.258-.966l.883-.237-1.12-.646a.5.5 0 1 1 .5-.866l1.12.646-.237-.883a.5.5 0 0 1 .966-.258l.495 1.849.94.542-.236-.883a.5.5 0 0 1 .966-.258l.495 1.849 1.236.713V5.707L6.147 4.354a.5.5 0 1 1 .707-.708l.646.647V3.207L6.147 1.854a.5.5 0 1 1 .707-.708l.646.647V.5a.5.5 0 0 1 1 0v1.293l.647-.647a.5.5 0 1 1 .707.708L8.5 3.207v1.086l.647-.647a.5.5 0 1 1 .707.708L8.5 5.707v1.427l1.236-.713.495-1.85a.5.5 0 1 1 .966.26l-.236.882.94-.542.495-1.85a.5.5 0 1 1 .966.26l-.236.882 1.12-.646a.5.5 0 0 1 .5.866l-1.12.646.883.237a.5.5 0 1 1-.26.966l-1.848-.495-.94.542.883.237a.5.5 0 1 1-.26.966l-1.848-.495L9 8l1.236.713 1.849-.495a.5.5 0 0 1 .259.966l-.883.237.94.542 1.849-.495a.5.5 0 0 1 .259.966l-.883.237 1.12.646a.5.5 0 0 1-.5.866l-1.12-.646.236.883a.5.5 0 1 1-.966.258l-.495-1.849-.94-.542.236.883a.5.5 0 0 1-.966.258L9.736 9.58 8.5 8.866v1.427l1.354 1.353a.5.5 0 0 1-.707.708l-.647-.647v1.086l1.354 1.353a.5.5 0 0 1-.707.708l-.647-.647V15.5a.5.5 0 0 1-.5.5"
                    />
                  </svg>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-cloud-sun-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M11.473 11a4.5 4.5 0 0 0-8.72-.99A3 3 0 0 0 3 16h8.5a2.5 2.5 0 0 0 0-5z"
                    />
                    <path
                      d="M10.5 1.5a.5.5 0 0 0-1 0v1a.5.5 0 0 0 1 0zm3.743 1.964a.5.5 0 1 0-.707-.707l-.708.707a.5.5 0 0 0 .708.708zm-7.779-.707a.5.5 0 0 0-.707.707l.707.708a.5.5 0 1 0 .708-.708zm1.734 3.374a2 2 0 1 1 3.296 2.198q.3.423.516.898a3 3 0 1 0-4.84-3.225q.529.017 1.028.129m4.484 4.074c.6.215 1.125.59 1.522 1.072a.5.5 0 0 0 .039-.742l-.707-.707a.5.5 0 0 0-.854.377M14.5 6.5a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1z"
                    />
                  </svg>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-sun-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"
                    />
                  </svg>
                </td>
                <td class="text-center">56% - 78.71 UAH</td>
                <td class="text-center">--</td>
                <td class="text-center">58% - 82.15 UAH</td>
                <td class="text-center">
                  <span class="badge text-bg-secondary">575.49W</span>
                </td>
                <td class="text-center">
                  <span class="badge text-bg-secondary">2.49UAH</span>
                </td>
                <td class="text-center">{{ power_tariff }}</td>
              </tr>

              <tr>
                <th scope="row" class="text-center">21.09.2025</th>
                <td class="text-center">400</td>
                <td class="text-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-sun-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M8 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"
                    />
                  </svg>
                </td>
                <td class="text-center">30% - 75.57 UAH</td>
                <td class="text-center">- -</td>
                <td class="text-center">56% - 78.71 UAH</td>
                <td class="text-center">
                  <span class="badge text-bg-secondary">997.56W</span>
                </td>
                <td class="text-center">
                  <span class="badge text-bg-secondary">4.31UAH</span>
                </td>
                <td class="text-center">4.32 UAH</td>
              </tr>
              <tr>
                <th scope="row" class="text-center">20.09.2025</th>
                <td class="text-center">400</td>
                <td class="text-center">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="16"
                    height="16"
                    fill="currentColor"
                    class="bi bi-cloud-fill"
                    viewBox="0 0 16 16"
                  >
                    <path
                      d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383"
                    />
                  </svg>
                </td>
                <td class="text-center">21% - 71.18 UAH</td>
                <td class="text-center">- -</td>
                <td class="text-center">30% - 75.57 UAH</td>
                <td class="text-center">
                  <span class="badge text-bg-secondary">938.75W</span>
                </td>
                <td class="text-center">
                  <span class="badge text-bg-secondary">4.06UAH</span>
                </td>
                <td class="text-center">4.32 UAH</td>
              </tr>
            </tbody>
          </table>
          <nav
            aria-label="Page navigation example"
            class="d-flex justify-content-center mt-2"
          >
            <ul class="pagination">
              <li class="page-item">
                <a class="page-link" href="#" aria-label="Previous">
                  <span aria-hidden="true">&laquo;</span>
                </a>
              </li>
              <li class="page-item"><a class="page-link" href="#">1</a></li>
              <li class="page-item"><a class="page-link" href="#">2</a></li>
              <li class="page-item"><a class="page-link" href="#">3</a></li>
              <li class="page-item">
                <a class="page-link" href="#" aria-label="Next">
                  <span aria-hidden="true">&raquo;</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
