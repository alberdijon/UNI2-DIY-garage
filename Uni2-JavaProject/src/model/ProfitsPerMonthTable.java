/*
 * This software has been developed by Uni2
 * Under the GNU General Public License
 */
package model;

import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

/**
 *
 * @author agirrezabala.peru
 */
public class ProfitsPerMonthTable extends AbstractTableModel {
    private ArrayList<ProfitsPerMonth> pmonth = new ArrayList<>();
    private final String[] columnName = {"Date","Total"};
    public ProfitsPerMonthTable(ArrayList<ProfitsPerMonth> profitable){
        this.pmonth=profitable;
    }

    @Override
    public int getRowCount() {
        return pmonth.size();
    }

    @Override
    public int getColumnCount() {
        return columnName.length;
    }
    public String getColumnName(int column){
        return columnName[column];
    }
    @Override
    public Object getValueAt(int rowIndex, int columnIndex) {
        switch(columnIndex){
            
            case 0: return pmonth.get(rowIndex).getDate();
            case 1: return pmonth.get(rowIndex).getTotalPrice();



            default: return null;
        }
    }
    
}
