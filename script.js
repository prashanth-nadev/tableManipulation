$(document).ready(function () {
    const tableBody = $('#employeeTable tbody');
    let data = [];
    let filteredData = [];
    let currentSortColumn = null;
    let isAscending = true;
    let currentPage = 1;
    const rowsPerPage = 10;

    function fetchAndPopulateData() {
        $.ajax({
            url: 'http://127.0.0.1:5000/data', dataType: 'json', success: function (response) {
                if (response && response.length > 0) {
                    data = response;
                    filteredData = data; 
                    populateTable(filteredData);
                    updatePagination();
                } else {
                    console.error('Data is empty or undefined.');
                }
            }, error: function (xhr, status, error) {
                console.error('Error fetching data:', status, error);
            }
        });
    }

    function populateTable(data) {
        tableBody.empty();

        const startIndex = (currentPage - 1) * rowsPerPage;
        const endIndex = startIndex + rowsPerPage;

        for (let i = startIndex; i < endIndex && i < data.length; i++) {
            const item = data[i];
            const row = $('<tr>');
            row.append($('<td>').text(item.first_name));
            row.append($('<td>').text(item.last_name));
            row.append($('<td>').text(item.department));
            row.append($('<td>').text(item.job_title));
            row.append($('<td>').text(item.salary));
            row.append($('<td>').text(item.email));
            row.append($('<td>').text(item.phone_number));
            tableBody.append(row);
        }
    }

    function sortTable(columnName) {
        if (currentSortColumn === columnName) {
            isAscending = !isAscending;
        } else {
            currentSortColumn = columnName;
            isAscending = true;
        }

        filteredData.sort(function (a, b) {
            const cellA = a[columnName].toString().toLowerCase();
            const cellB = b[columnName].toString().toLowerCase();
            return isAscending ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
        });

        populateTable(filteredData);
        updatePagination();
    }

    function updatePagination() {
        const totalPages = Math.ceil(filteredData.length / rowsPerPage);

        // fpr updating pagination controls
        const pagination = $('<div class="pagination">');
        for (let i = 1; i <= totalPages; i++) {
            const pageLink = $('<a>');
            pageLink.text(i);
            pageLink.on('click', function () {
                currentPage = i;
                populateTable(filteredData);
            });
            pagination.append(pageLink);
        }

        // append the pagination in page
        $('.pagination').remove(); 
        $('#employeeTable').after(pagination);
    }

    $('#employeeTable thead th').each(function () {
        const columnName = $(this).data('column');
        $(this).on('click', function () {
            sortTable(columnName);
        });
    });

    $('#search-button').on('click', function () {
        const searchTerm = $('#search-input').val().toLowerCase();
        if (searchTerm.trim() === '') {
            filteredData = data;
        } else {
            filteredData = data.filter(function (item) {
                return (item.first_name.toLowerCase().includes(searchTerm) || item.last_name.toLowerCase().includes(searchTerm) || item.department.toLowerCase().includes(searchTerm) || item.job_title.toLowerCase().includes(searchTerm) || item.salary.toString().includes(searchTerm) || item.email.toLowerCase().includes(searchTerm) || item.phone_number.includes(searchTerm));
            });
        }

        currentPage = 1;
        populateTable(filteredData);
        updatePagination();


    });

    $('#reset-button').on('click', function () {
        window.location.reload();
    });

    fetchAndPopulateData();
});

