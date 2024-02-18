import { Table, TableBody, TableCaption, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { FC } from "react";

interface LeaderboardTableProps {
    data: {
        id: number;
        name: string;
        score: number;
    }[];
}

export const LeaderboardTable: FC<LeaderboardTableProps> = ({ data }) => {
    return (<>
        <Table>
            <TableCaption>A list of your recent invoices.</TableCaption>
            <TableHeader>
                <TableRow>
                    <TableHead className="w-[120px]">Bot Name</TableHead>
                    <TableHead>Wins</TableHead>
                    <TableHead>Draws</TableHead>
                    <TableHead>Losses</TableHead>
                    <TableHead className="text-right">Score</TableHead>
                </TableRow>
            </TableHeader>
            <TableBody>
                <TableRow>
                    <TableCell className="font-medium">INV001</TableCell>
                    <TableCell>Paid</TableCell>
                    <TableCell>Credit Card</TableCell>
                    <TableCell className="text-right">$250.00</TableCell>
                </TableRow>
            </TableBody>
        </Table>
    </>)
}